#!/usr/bin/env python3
"""Synthetic unit inputs, not practice dossiers or real client data."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


journal = module('kanzlei')
deadline = module('fristen_at')


class JournalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder, self.con = journal.connect(self.temp.name, create=True)
        self.addCleanup(self.con.close)
        self.addCleanup(self.temp.cleanup)
        self.matter = json.loads((ROOT / 'assets/mandat-beispiel.json').read_text())
        self.terms = json.loads((ROOT / 'assets/honorar-beispiel.json').read_text())
        self.time = json.loads((ROOT / 'assets/zeit-beispiel.json').read_text())
        journal.init(self.con, self.matter)
        journal.add_terms(self.con, self.terms)

    def test_austrian_amount_and_real_files(self):
        journal.add_entry(self.con, 'time', self.time)
        result = journal.snapshot(self.con)
        self.assertEqual((result['known_net_eur'], result['known_vat_eur'], result['known_gross_eur']), ('72.00', '14.40', '86.40'))
        self.assertFalse(result['invoice_ready'])
        journal.export(self.folder, result)
        self.assertTrue((self.folder / '03_ERV_Vorbereitung').is_dir())
        self.assertFalse((self.folder / '03_beA_Vorbereitung').exists())
        saved = json.loads((self.folder / '02_Honorar/rechnungsentwurf.json').read_text())
        self.assertEqual(saved['known_vat_eur'], '14.40')
        self.assertIn('Umsatzsteuer 20 %', (self.folder / '02_Honorar/rechnungsentwurf.md').read_text())

    def test_reject_german_vat_and_tax_assumptions(self):
        for key, value in [('vat_rate', '19'), ('jurisdiction', 'DE'), ('tax_reviewed', False), ('tax_basis_ref', '')]:
            terms = copy.deepcopy(self.terms)
            terms['id'] = 'INVALID'
            terms[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                journal.add_terms(self.con, terms)

    def test_reject_foreign_existing_journal(self):
        german = copy.deepcopy(self.matter)
        german['jurisdiction'] = 'DE'
        self.con.execute('UPDATE matter SET data=?', (json.dumps(german),))
        with self.assertRaises(ValueError):
            journal.snapshot(self.con)

    def test_idempotence_and_correction(self):
        journal.add_entry(self.con, 'time', self.time)
        revision = journal.snapshot(self.con)['journal_revision']
        journal.add_entry(self.con, 'time', self.time)
        self.assertEqual(journal.snapshot(self.con)['journal_revision'], revision)
        changed = dict(self.time, minutes=19)
        with self.assertRaises(ValueError):
            journal.add_entry(self.con, 'time', changed)
        journal.void(self.con, 'Z1', 'Dauer berichtigt')
        journal.add_entry(self.con, 'time', dict(changed, id='Z2'))
        self.assertEqual(journal.snapshot(self.con)['known_net_eur'], '76.00')

    def test_pending_time_does_not_become_zero_or_charge(self):
        pending = dict(self.time, confirmed=False)
        del pending['minutes']
        journal.add_entry(self.con, 'time', pending)
        result = journal.snapshot(self.con)
        self.assertEqual(result['known_net_eur'], '0.00')
        self.assertFalse(result['complete'])
        self.assertIsNone(result['entries'][0]['data']['minutes'])

    def test_tariff_requires_legal_review_and_source(self):
        journal.add_terms(self.con, dict(self.terms, id='T1', model='tariff'))
        entry = {'id':'F1', 'terms_id':'T1', 'source':'synthetic input', 'confirmed':True,
                 'date':'2026-10-07', 'description':'Isolierter geprüfter Tarifwert',
                 'net_eur':'100.00', 'legal_reviewed':True}
        with self.assertRaises(ValueError):
            journal.add_entry(self.con, 'manual-fee', entry)
        journal.add_entry(self.con, 'manual-fee', dict(entry, tariff_basis_ref='Synthetische geprüfte Bewertung'))
        self.assertEqual(journal.snapshot(self.con)['known_gross_eur'], '120.00')
        journal.add_terms(self.con, dict(self.terms, id='H2', model='hourly'))
        with self.assertRaises(ValueError):
            journal.add_entry(self.con, 'manual-fee', dict(entry, id='F2', terms_id='H2', tariff_basis_ref='source'))

    def test_german_tariff_rejected(self):
        with self.assertRaises(ValueError):
            journal.add_terms(self.con, dict(self.terms, id='GER', model='rvg'))

    def test_payments_and_fremdgeld_do_not_offset_invoice(self):
        journal.add_entry(self.con, 'time', self.time)
        journal.add_entry(self.con, 'payment', {'id':'P1','source':'synthetic','confirmed':True,
            'date':'2026-10-07','reference':'isolated third party funds','kind':'third_party','gross_eur':'1000.00'})
        result = journal.snapshot(self.con)
        self.assertEqual(result['known_gross_eur'], '86.40')
        self.assertEqual(result['payments'][0]['kind'], 'third_party')

    def test_capped_and_flat_amounts(self):
        journal.add_terms(self.con, dict(self.terms, id='CAP', model='capped', cap_eur='50.00', cap_scope='fees_only'))
        journal.add_entry(self.con, 'time', dict(self.time, terms_id='CAP'))
        self.assertEqual(journal.snapshot(self.con)['known_gross_eur'], '60.00')
        journal.add_terms(self.con, dict(self.terms, id='FLAT', model='flat', flat_eur='100.00'))
        journal.add_entry(self.con, 'time', dict(self.time, id='Z2', terms_id='FLAT', minutes=10))
        self.assertEqual(journal.snapshot(self.con)['known_gross_eur'], '180.00')

    def test_used_phase_cannot_be_revalued(self):
        journal.add_entry(self.con, 'time', self.time)
        with self.assertRaises(ValueError):
            journal.add_terms(self.con, dict(self.terms, rate_eur='500.00'))


def profile(trigger='2026-03-20', regime='zpo', amount=2, unit='weeks'):
    # This calendar only covers the range needed by the isolated Good-Friday
    # example; it is a fixture, not a published complete annual calendar.
    return {'schema_version':1, 'matter_id':'SYNTHETIC', 'jurisdiction':'AT',
        'regime':regime, 'trigger':trigger, 'amount':amount, 'unit':unit,
        'legal_reviewed':True, 'trigger_reviewed':True, 'exceptions_reviewed':True,
        'special_rules':'none_applicable_confirmed', 'rule_source':'isolated regular profile',
        'trigger_source':'synthetic event', 'calendar':{'place':'synthetic local calendar',
        'source':'unit-test fixture', 'verified':True, 'valid_from':'2026-03-01',
        'valid_to':'2026-04-30', 'holidays':[{'date':'2026-04-06','name':'Ostermontag'}]}}


class DeadlineTests(unittest.TestCase):
    def test_good_friday_and_easter_monday(self):
        result = deadline.calculate(profile())
        self.assertEqual(result['unadjusted_end'], '2026-04-03')
        self.assertEqual(result['end'], '2026-04-07')
        self.assertFalse(result['calendar_saved'])
        self.assertIn('Karfreitag', result['excluded_end_days'][0]['reasons'][0])

    def test_christmas_eve_differs_between_zpo_and_avg(self):
        p = profile('2026-12-10')
        p['calendar'].update(valid_from='2026-12-01', valid_to='2026-12-31',
            holidays=[{'date':'2026-12-25','name':'Christtag'},{'date':'2026-12-26','name':'Stefanitag'}])
        self.assertEqual(deadline.calculate(p)['end'], '2026-12-24')
        p['regime'] = 'avg'
        self.assertEqual(deadline.calculate(p)['end'], '2026-12-28')

    def test_month_end_and_leap_year(self):
        p = profile('2026-01-31', amount=1, unit='months')
        p['calendar'].update(valid_from='2026-01-01', valid_to='2026-03-05', holidays=[])
        result = deadline.calculate(p)
        self.assertEqual(result['unadjusted_end'], '2026-02-28')
        self.assertEqual(result['end'], '2026-03-02')
        p['trigger'] = '2024-01-31'
        p['calendar'].update(valid_from='2024-01-01', valid_to='2024-03-05')
        self.assertEqual(deadline.calculate(p)['end'], '2024-02-29')

    def test_day_trigger_is_excluded(self):
        self.assertEqual(deadline.calculate(profile('2026-03-02', amount=1, unit='days'))['end'], '2026-03-03')

    def test_unreviewed_or_unsupported_profiles_rejected(self):
        for key, value in [('regime','bao'), ('jurisdiction','DE'), ('unit','hours'),
            ('legal_reviewed',False), ('trigger_reviewed',False), ('exceptions_reviewed',False),
            ('special_rules','interruption'), ('amount',True), ('amount',0)]:
            p = profile()
            p[key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                deadline.calculate(p)

    def test_calendar_must_cover_shifted_end_and_be_reviewed(self):
        p = profile()
        p['calendar']['valid_to'] = '2026-04-06'
        with self.assertRaises(ValueError):
            deadline.calculate(p)
        p = profile()
        p['calendar']['verified'] = False
        with self.assertRaises(ValueError):
            deadline.calculate(p)

    def test_duplicates_and_missing_list_rejected(self):
        p = profile()
        p['calendar']['holidays'] *= 2
        with self.assertRaises(ValueError):
            deadline.calculate(p)
        p = profile()
        del p['calendar']['holidays']
        with self.assertRaises(ValueError):
            deadline.calculate(p)

    def test_output_preserves_existing_file(self):
        with tempfile.TemporaryDirectory() as name:
            source = Path(name)/'input.json'
            target = Path(name)/'existing.json'
            source.write_text(json.dumps(profile()))
            target.write_text('original')
            result = subprocess.run([sys.executable, str(ROOT/'scripts/fristen_at.py'),
                '--data', str(source), '--out', str(target)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(target.read_text(), 'original')


if __name__ == '__main__':
    unittest.main(verbosity=2)
