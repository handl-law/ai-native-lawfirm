#!/usr/bin/env python3
"""Validate only the Austrian package, without loading German collections."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate():
    manifest = json.loads((ROOT / 'plugin.json').read_text())
    assert manifest['name'] == ROOT.name == 'ki-native-kanzlei-at'
    assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
    interface = manifest['extensions']['com.openai']['interface']
    assert len(interface['shortDescription']) <= 30
    assert 'apps' not in manifest['extensions']['com.openai']
    assert not ({'skills', 'mcpServers', 'apps', 'interface'} & manifest.keys())
    expected = {
        'ki-kanzlei-steuern', 'mandatsannahme-interessenkollision',
        'akte-fristen-anlegen', 'fristen-berechnen-ueberwachen',
        'anwaltsberufsrecht-pruefen', 'geldwaesche-pruefen',
        'honorar-budget-vereinbaren', 'zeiten-erfassen', 'workflow-uebergabe',
        'recht-recherchieren', 'schriftsaetze-entwerfen', 'vertraege-agb-pruefen',
        'vertraege-gestalten', 'mandantenkommunikation', 'erv-beilagen-vorbereiten',
        'abrechnung-e-rechnung', 'zahlungen-buchhaltung', 'mandat-abschliessen'
    }
    paths = list((ROOT / 'skills').glob('*/SKILL.md'))
    assert {p.parent.name for p in paths} == expected
    for path in paths:
        content = path.read_text()
        frontmatter = content.split('---', 2)[1]
        fields = dict(line.split(':', 1) for line in frontmatter.strip().splitlines())
        assert set(fields) == {'name', 'description'}, path
        assert fields['name'].strip() == path.parent.name
        assert len(fields['description']) <= 1024
        for n in range(1, 7):
            assert f'## {n}. ' in content, path
        assert 'ausformulierten Sätzen' in content and '11 pt' in content
    for path in ROOT.rglob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
                continue
            target = (path.parent / link.split('#', 1)[0]).resolve()
            assert target.is_relative_to(ROOT) and target.exists(), (path, link)
    for path in ROOT.rglob('*'):
        assert not path.is_symlink(), path
    for name in ('LICENSE', 'LICENSE-APACHE', 'LICENSE-MIT', 'NOTICE', 'UPSTREAM.json'):
        assert (ROOT / name).is_file(), name
    marketplace_path = ROOT.parent / '.claude-plugin/marketplace.json'
    if marketplace_path.is_file():
        marketplace = json.loads(marketplace_path.read_text())
        entries = [p for p in marketplace['plugins'] if p['name'] == manifest['name']]
        assert len(entries) == 1 and entries[0]['source'] == './ki-native-kanzlei-at'
        assert entries[0]['version'] == manifest['version']
    print('PASS: 18 Skills, Manifest, lokale Links, Herkunft/Lizenzen und Marketplace-Eintrag')


if __name__ == '__main__':
    validate()
