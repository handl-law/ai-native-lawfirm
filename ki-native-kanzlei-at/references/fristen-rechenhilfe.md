# 1. Österreichische Fristen-Rechenhilfe

Neuer österreichischer Helfer, handl-law, 7. Oktober 2026. Die deutsche Rechenhilfe wurde nicht übernommen. Python 3.10 oder neuer und Standardbibliothek genügen.

## 1.1. Unterstützter Umfang

`scripts/fristen_at.py` rechnet ausschließlich reguläre, zuvor rechtlich geprüfte ZPO- oder AVG-Profile nach Tagen, Wochen, Monaten oder Jahren. Das Ereignis-/Zustelldatum und die Fristlänge müssen schon geprüft sein. Die bloße Angabe `regime=avg` bestätigt nicht die Anwendbarkeit im verwaltungsgerichtlichen, steuerlichen oder sonstigen Verfahren. Spezialfristen, materielle Fristen, verhandlungsfreie Zeiten, Unterbrechung/Hemmung, Stunden, Werktage und fixe Uhrzeiten werden nicht unterstützt.

Bei Tagesfristen wird der auslösende Tag ausgeschlossen; Wochen-/Monats-/Jahresfristen enden kalenderbezogen am korrespondierenden Tag, bei fehlendem Monatstag am Monatsletzten. Endverschiebung: im ZPO-Profil Samstag, Sonntag, bereitgestellte Feiertage und Karfreitag; im AVG-Profil zusätzlich 24. Dezember. Karfreitag wird mittels gregorianischer Osterrechnung ermittelt, nicht als allgemeiner gesetzlicher Feiertag bezeichnet. Quellen: [§ 125 ZPO](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001699&Paragraf=125), [§ 126 ZPO](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001699&Paragraf=126), [§ 32 AVG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005768&Paragraf=32), [§ 33 AVG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005768&Paragraf=33). Grundlagen abgerufen am 7. Oktober 2026; Anwendbarkeit und späterer Stand sind fallbezogen zu prüfen.

## 1.2. Eingabe

JSON-Objekt: schema_version=1, jurisdiction=AT, matter_id, regime=zpo/avg, trigger als YYYY-MM-DD, amount als positive ganze Zahl und unit=days/weeks/months/years. Zusätzlich erforderlich: rule_source mit konkreter Frist-/Verfahrensnorm und Fassung, trigger_source mit Originalzustell-/Ereignisbeleg, legal_reviewed=true, trigger_reviewed=true, exceptions_reviewed=true und special_rules=none_applicable_confirmed. Flags erst nach tatsächlicher fachlicher Prüfung setzen; das Programm bestätigt deren Wahrheit nicht.

calendar enthält place, source, valid_from, valid_to, verified=true und holidays als vollständige ausdrücklich geprüfte Liste von Objekten mit date und name. Die örtlich einschlägigen gesetzlichen Feiertage müssen im gesamten angegebenen Zeitraum enthalten sein; keine automatische Landes-/Feiertagsrecherche. Ein leeres Array behauptet ausdrücklich, dass in genau diesem geprüften Zeitraum keine einschlägigen gesetzlichen Feiertage vorkommen. Fehlende Feiertage kann das Programm nicht erkennen. Der Zeitraum muss Trigger, rechnerisches Ende und sämtliche Verschiebetage abdecken; sonst bricht die Rechnung ab.

## 1.3. Ausführen und kontrollieren

```bash
python3 scripts/fristen_at.py --data /pfad/geprueftes-profil.json --out /pfad/neuer-fristenvermerk.json
```

Das Ausgabeziel darf noch nicht existieren. Ohne --out wird nur JSON ausgegeben. Input-Hash identifiziert die übergebene JSON-Eingabe, nicht die originale Zustellurkunde. Ausgabe enthält unverschobenes und angepasstes Ende sowie ausgeschlossene Endtage. `calendar_saved` ist immer false. Kontrolliere die Rechnung unabhängig und speichere Vorfrist, Ende und Vertretung im tatsächlich eingesetzten Kanzleikalender. Das Programm bestimmt weder Zustellzeitpunkt noch Fristlänge oder Fristwahrung; diese Prüfungen und tatsächliches Einlangen bleiben außerhalb.
