#!/usr/bin/env python3
"""Österreichische Kalenderhilfe, handl-law, 7. Oktober 2026.

SPDX-License-Identifier: Apache-2.0 OR MIT
Reguläre ausdrücklich geprüfte ZPO-/AVG-Fristen, keine Rechtswahl, Zustellungs-
prüfung, Unterbrechung, Spezialfrist, Uhrzeit oder Kalendersynchronisierung.
"""
import argparse
import calendar
import hashlib
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path


def text(obj, key):
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
        raise ValueError(f'{key}: eindeutiger einzeiliger Text erforderlich')
    return value


def day(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError('Datum muss YYYY-MM-DD sein')
    result = date.fromisoformat(value)
    if result.year < 1583:
        raise ValueError('Nur gregorianische Kalenderjahre ab 1583 unterstützt')
    return result


def good_friday(year):
    """Gregorian Easter computus; Good Friday is two days before Easter."""
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month, offset = divmod(h + l - 7 * m + 114, 31)
    return date(year, month, offset + 1) - timedelta(days=2)


def calculate(data):
    if not isinstance(data, dict) or type(data.get('schema_version')) is not int or data['schema_version'] != 1:
        raise ValueError('schema_version=1 erforderlich')
    matter = text(data, 'matter_id')
    if data.get('jurisdiction') != 'AT':
        raise ValueError('Nur jurisdiction=AT unterstützt')
    regime = text(data, 'regime')
    if regime not in ('zpo', 'avg'):
        raise ValueError('Nur reguläre zpo- oder avg-Fristen unterstützt')
    for key in ('legal_reviewed', 'trigger_reviewed', 'exceptions_reviewed'):
        if data.get(key) is not True:
            raise ValueError(f'{key}=true nach tatsächlicher vorgelagerter Prüfung erforderlich')
    if data.get('special_rules') != 'none_applicable_confirmed':
        raise ValueError('Spezialregeln, Hemmung und Unterbrechung nicht unterstützt')
    basis = text(data, 'rule_source')
    trigger_source = text(data, 'trigger_source')
    trigger = day(text(data, 'trigger'))
    amount = data.get('amount')
    if type(amount) is not int or not 1 <= amount <= 36600:
        raise ValueError('amount: ganze positive Zahl bis 36600 erforderlich')
    unit = text(data, 'unit')
    if unit not in ('days', 'weeks', 'months', 'years'):
        raise ValueError('Nur days, weeks, months, years; keine Stunden-/Werktagsfristen')

    cal = data.get('calendar')
    if not isinstance(cal, dict) or cal.get('verified') is not True:
        raise ValueError('Vollständiger, ausdrücklich geprüfter Feiertagskalender erforderlich')
    place, calendar_source = text(cal, 'place'), text(cal, 'source')
    first, last = day(text(cal, 'valid_from')), day(text(cal, 'valid_to'))
    if first > last:
        raise ValueError('Kalenderzeitraum widersprüchlich')
    rows = cal.get('holidays')
    if not isinstance(rows, list):
        raise ValueError('holidays: explizite vollständige Liste erforderlich')
    holidays = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {'date', 'name'}:
            raise ValueError('Feiertag benötigt genau date und name')
        holiday = day(text(row, 'date'))
        if not first <= holiday <= last or holiday in holidays:
            raise ValueError('Feiertag außerhalb Kalenderzeitraum oder doppelt')
        holidays[holiday] = text(row, 'name')

    def coverage(value):
        if not first <= value <= last:
            raise ValueError(f'Kalender deckt {value} nicht ab')

    coverage(trigger)
    try:
        if unit in ('days', 'weeks'):
            end = trigger + timedelta(days=amount * (7 if unit == 'weeks' else 1))
        else:
            months = amount * (12 if unit == 'years' else 1)
            index = trigger.year * 12 + trigger.month - 1 + months
            year, month = divmod(index, 12)
            month += 1
            if not 1583 <= year <= 9999:
                raise ValueError('Endjahr außerhalb unterstütztem Bereich')
            end = date(year, month, min(trigger.day, calendar.monthrange(year, month)[1]))
        coverage(end)
        unadjusted = end
        excluded = []
        while True:
            coverage(end)
            reasons = []
            if end.weekday() >= 5:
                reasons.append('Samstag' if end.weekday() == 5 else 'Sonntag')
            if end in holidays:
                reasons.append(holidays[end])
            if end == good_friday(end.year):
                reasons.append('Karfreitag: besonderer verfahrensrechtlicher Endtag')
            if regime == 'avg' and end.month == 12 and end.day == 24:
                reasons.append('24. Dezember: besonderer Endtag nach § 33 AVG')
            if not reasons:
                break
            excluded.append({'date': end.isoformat(), 'reasons': reasons})
            end += timedelta(days=1)
    except OverflowError:
        raise ValueError('Frist außerhalb unterstütztem Datumsbereich') from None

    canonical = json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
    return {
        'matter_id': matter, 'jurisdiction': 'AT', 'regime': regime,
        'status': 'Rechenvermerk; keine rechtliche oder kalendarische Freigabe',
        'rule_source': basis, 'trigger_source': trigger_source,
        'trigger': trigger.isoformat(), 'amount': amount, 'unit': unit,
        'unadjusted_end': unadjusted.isoformat(), 'end': end.isoformat(),
        'excluded_end_days': excluded, 'calendar_place': place,
        'calendar_source': calendar_source,
        'input_sha256': hashlib.sha256(canonical.encode()).hexdigest(),
        'calendar_saved': False,
        'notice': 'Prüfflags sind Angaben des Bearbeiters, keine maschinelle Bestätigung. Keine Prüfung der Fristlänge, Zustellung, Feiertagsvollständigkeit, Spezialregeln oder Rechtzeitigkeit des Übermittlungswegs.'
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', required=True, type=Path)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    result = calculate(json.loads(args.data.read_text(encoding='utf-8')))
    content = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    if args.out:
        # Exclusive creation preserves any existing computation.
        with args.out.open('x', encoding='utf-8') as stream:
            stream.write(content)
    else:
        print(content, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, TypeError) as exc:
        print(f'Fehler: {exc}', file=sys.stderr)
        sys.exit(2)
