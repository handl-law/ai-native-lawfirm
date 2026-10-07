---
name: zahlungen-buchhaltung
description: "Ordnet belegte österreichische Mandatszahlungen, Vorschüsse und Fremdgeld zu und bereitet nachvollziehbare Buchhaltungsvorschläge vor."
---

# Zahlungen und Buchhaltung vorbereiten

Österreichische Neufassung für handl-law, 7. Oktober 2026, auf Grundlage der Workflow-Struktur von Klotzkette. Version 0.1.0; keine behauptete fachliche Freigabe.

## 1. Zweck und Anwendungsfall

Ordnet belegte österreichische Mandatszahlungen, Vorschüsse und Fremdgeld zu und bereitet nachvollziehbare Buchhaltungsvorschläge vor. Lies vor der Bearbeitung [Arbeitsweise](../../references/arbeitsweise.md). Österreichische Sach-, Verfahrens- und Berufsregeln gehen deutschen Vorlagen aus dem Quellrepository vor. Bei Auslandsbezug ist die Rechtswahl gesondert zu bestimmen.

## 2. Eingaben

Bankbeleg, Betrag, Valuta, Zahler, Referenz, Honorarnote, Honorarphase, Zahlungszweck und gegebenenfalls Treuhandauftrag. Lies vorhandene Unterlagen zuerst und übernimm bereits bestätigte Antworten. Stelle nur Rückfragen, deren Antwort das konkrete Ergebnis verändert. Fehlende Tatsachen bleiben ausdrücklich offen.

## 3. Ablauf / Checkliste

### 3.1. Bearbeitungsschritt

Lies Originalbeleg und bestimme Mandats- und Rechnungszuordnung; Zahlungszweck oder Zahler sind nicht ohne Nachweis aus einer ähnlichen Buchung zu übernehmen.

### 3.2. Bearbeitungsschritt

Trenne Honorareingang, Vorschuss, Gerichtskosten und echtes Fremd-/Treuhandgeld. Wende aktuelle RAO, Kammer-/Treuhandregeln und Steuerrecht auf die jeweilige Kategorie an.

### 3.3. Bearbeitungsschritt

Prüfe bei Vorschüssen Leistungsstand, gegebenenfalls Anzahlungsrechnung und Steuerwirkung; bei durchlaufenden Posten und Auslagen prüfe tatsächlichen Rechts- und Steuercharakter.

### 3.4. Bearbeitungsschritt

Erfasse nur bestätigte Geldflüsse im Journal. payments werden separat ausgewiesen und nicht automatisch mit Honorar oder Steuer verrechnet; bestätigte Fremdgelder sind keine Umsatzerlöse.

### 3.5. Bearbeitungsschritt

Erstelle eine belegte Zuordnungs- und Buchungsempfehlung nach dem tatsächlich eingesetzten österreichischen Kontenrahmen. Kontonummern nicht ohne Kanzleivorgabe erfinden.

### 3.6. Bearbeitungsschritt

Dokumentiere offene Differenzen und erforderliche Freigabe der tatsächlichen Buchung oder Verfügung. Das lokale SQLite-Journal ist weder Hauptbuch noch manipulationssicheres gesetzliches Archiv.

## 4. Quellenpflicht

Es gelten die österreichische [Zitierweise](../../references/zitierweise.md) und der [Quellenplan](../../references/rechtsquellen.md). Prüfe den vollständigen Norm- oder Entscheidungstext zum maßgeblichen Zeitpunkt. Keine Geschäftszahl, RS-Nummer, Randziffer oder Literaturfundstelle aus bloßem Modellwissen. Ein Link oder Suchtreffer ist noch kein Beleg seiner rechtlichen Anwendung; fehlender Zugriff bleibt als konkreter Prüfbedarf sichtbar.

## 5. Ausgabeformat

Ausformulierter Zahlungs-/Buchungsvermerk und strukturierte Belegzuordnung; tatsächliche Buchung und Verfügung getrennt. Das Endprodukt wird vollständig in grammatikalisch ausformulierten Sätzen erstellt; Skelette, Halbsätze und bloße Aufzählungen ersetzen keine Endfassung. Tabellen für tatsächlich parallele Angaben sind zulässig. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Markdown-Ausgabe steht ein nötiger Exporthinweis getrennt vom Empfängertext. Technische Prüfnotizen und Quellenprotokolle gehören nicht in den versandfertigen Text.

Kontrolliere vor Abschluss Produkt, Fakten, österreichische Rechtswahl, Quellenstatus, Zahlen, Fristen und tatsächlich gespeicherte Fassung. Eine technisch nicht ausgeführte Speicherung, Kalendereintragung, Buchung oder Übermittlung darf nicht als erledigt bezeichnet werden.

## 6. Beispiel

Ein Zahlungseingang von 500 EUR ist mit Mandatsnummer, aber ohne Rechnungsnummer bezeichnet. Prüfe, ob Vorschuss, Honorar oder Fremdgeld vorliegt.
