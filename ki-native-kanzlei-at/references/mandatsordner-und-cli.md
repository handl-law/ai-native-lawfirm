# 1. Lokaler österreichischer Mandatshelfer

Geänderter Helfer aus Klotzkettes deutschem Paket. Python 3.10 oder neuer, ausschließlich Standardbibliothek; keine Netzwerkaufrufe oder Hintergrunddienste. Journal ist führend: `00_Mandat/mandatsjournal.sqlite`. Arbeitsprodukte: `01_Bearbeitung`; Entwürfe/CSV: `02_Honorar`; vorbereitete ERV-Dateien: `03_ERV_Vorbereitung`.

## 1.1. Isolierte Rechendemonstration

Die drei JSON-Dateien sind synthetische Recheneingaben, keine echte Mandats- oder Testakte. Die Steuerprüfung wird dort als Annahme demonstriert, nicht als fachlich durchgeführte Prüfung für einen realen Umsatz. Verwende einen neuen leeren Demonstrationsordner.

```bash
python3 scripts/kanzlei.py init --akte /tmp/at-journal-demo --data assets/mandat-beispiel.json
python3 scripts/kanzlei.py terms --akte /tmp/at-journal-demo --data assets/honorar-beispiel.json
python3 scripts/kanzlei.py time --akte /tmp/at-journal-demo --data assets/zeit-beispiel.json
python3 scripts/kanzlei.py status --akte /tmp/at-journal-demo
```

Erwartet: 18 Minuten zu 240 EUR/h ergeben 72 EUR netto, 14.40 EUR USt und 86.40 EUR brutto. JSON, Markdown und Zeiten-CSV werden tatsächlich gespeichert. `invoice_ready` bleibt false. Wiederholung desselben IDs mit identischen Angaben verändert keine Buchung.

## 1.2. Honorarphasen und Bestätigung

`model`: hourly, capped, estimate, flat oder tariff. Jede Phase benötigt id, scope, agreement_ref, confirmed, jurisdiction=AT, tax_reviewed=true, tax_basis_ref und vat_rate=20. hourly benötigt rate_eur; capped zusätzlich cap_eur und cap_scope=fees_only oder fees_and_expenses; estimate zusätzlich estimate_eur; flat benötigt flat_eur. Alle Beträge sind netto in EUR. Steuergrundlage tatsächlich vorab prüfen, nicht aus dem Beispiel übernehmen. Befreiung, Reverse Charge oder andere Steuersätze werden nicht unterstützt und nicht in 20 % umgerechnet.

## 1.3. Tarife und Korrekturen

Tarifphase `tariff` berechnet keine RATG-/AHK-Tabelle. Eine manuelle Position wird mit `manual-fee` eingetragen und benötigt id, terms_id, source, confirmed, date, description, net_eur, legal_reviewed=true und tariff_basis_ref als konkrete Quelle der zuvor geprüften Bewertung. Zeiten erzeugen keine Tarifgebühr. Die Kanzlei bestätigt RATG-/AHK-Anwendbarkeit, Bemessungsgrundlage, Tarifpost, Leistungszeitpunkt und Zuschläge außerhalb des Programms.

Mit `void --akte ... --id Z1 --reason 'Konkreter Korrekturgrund'` wird ein Eintrag nachvollziehbar storniert; neue Werte erhalten neue ID. Zahlungen benötigen id, source, confirmed, date, reference, kind=payment/advance/third_party und gross_eur; keine automatische Verrechnung. expense benötigt terms_id, date, description, net_eur und tax_classification=own_taxable; durchlaufende Posten und andere Steuerfälle sind außerhalb dieses Helfers zu bearbeiten.

## 1.4. Grenzen

Vorhandene deutsche Journaldateien nicht verwenden. Der Helfer lehnt fremde Jurisdiktion und ungeprüfte oder 19%-Honorarphasen ab. Die lokale SQLite-Datei ist weder ein rechtskonformes Hauptbuch noch ein manipulationssicheres Archiv. Entwurf ist keine ausgestellte Honorarnote; kein ebInterface-/UBL-XML, keine Buchung und kein ERV-Versand entstehen.
