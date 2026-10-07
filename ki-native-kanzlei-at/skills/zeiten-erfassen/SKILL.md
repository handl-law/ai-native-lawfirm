---
name: zeiten-erfassen
description: "Erfasst bestätigte tatsächliche Arbeitszeit in österreichischen Mandaten und aktualisiert den lokalen Rechnungsentwurf."
---

# Tatsächliche Zeit erfassen

Österreichische Neufassung für handl-law, 7. Oktober 2026, auf Grundlage der Workflow-Struktur von Klotzkette. Version 0.1.0; keine behauptete fachliche Freigabe.

## 1. Zweck und Anwendungsfall

Erfasst bestätigte tatsächliche Arbeitszeit in österreichischen Mandaten und aktualisiert den lokalen Rechnungsentwurf. Lies vor der Bearbeitung [Arbeitsweise](../../references/arbeitsweise.md). Österreichische Sach-, Verfahrens- und Berufsregeln gehen deutschen Vorlagen aus dem Quellrepository vor. Bei Auslandsbezug ist die Rechtswahl gesondert zu bestimmen.

## 2. Eingaben

Mandatskennung, Tag, Person, tatsächliche Minuten, Narrativ, Abrechenbarkeit, Quelle und Honorarphase. Lies vorhandene Unterlagen zuerst und übernimm bereits bestätigte Antworten. Stelle nur Rückfragen, deren Antwort das konkrete Ergebnis verändert. Fehlende Tatsachen bleiben ausdrücklich offen.

## 3. Ablauf / Checkliste

### 3.1. Bearbeitungsschritt

Übernimm konkrete Angaben und frage nur nach fehlendem Datum, Minuten, Narrativ, Person, Abrechenbarkeit oder Phase. Schätze keine Zeit aus Dokumentlänge oder hypothetischer manueller Arbeit.

### 3.2. Bearbeitungsschritt

Formuliere ein sachliches Narrativ zur tatsächlich beschriebenen Tätigkeit. Kontrolliere Doppelbuchungen, Tagesgesamtzeit und Übereinstimmung mit dem Auftrag.

### 3.3. Bearbeitungsschritt

Trenne bestätigte Zeit von offenen Angaben. Fehlende Dauer bleibt unbekannt, nicht null Minuten; eine unbestätigte Erfassung erhöht den bekannten Rechnungsbetrag nicht.

### 3.4. Bearbeitungsschritt

Prüfe die zugeordnete Honorarphase. Bei Pauschale dient Zeit der Nachkalkulation, bei Tarifphase ersetzt sie keine eigenständige RATG-/AHK-Prüfung.

### 3.5. Bearbeitungsschritt

Nutze bei verfügbarem Dateizugriff scripts/kanzlei.py mit eindeutiger ID und Quellenangabe. Identische Wiederholung ist idempotent; Korrektur erfolgt durch Storno mit Grund und neue ID.

### 3.6. Bearbeitungsschritt

Kontrolliere gespeicherte Zeitliste, Journalrevision und Entwurf. Ein gespeicherter Entwurf ist keine ausgestellte Honorarnote und keine Finanzbuchung.

## 4. Quellenpflicht

Es gelten die österreichische [Zitierweise](../../references/zitierweise.md) und der [Quellenplan](../../references/rechtsquellen.md). Prüfe den vollständigen Norm- oder Entscheidungstext zum maßgeblichen Zeitpunkt. Keine Geschäftszahl, RS-Nummer, Randziffer oder Literaturfundstelle aus bloßem Modellwissen. Ein Link oder Suchtreffer ist noch kein Beleg seiner rechtlichen Anwendung; fehlender Zugriff bleibt als konkreter Prüfbedarf sichtbar.

## 5. Ausgabeformat

Bestätigter Zeitdatensatz, präzises Narrativ und tatsächlich aktualisierter Honorarstand; offene Angaben getrennt. Das Endprodukt wird vollständig in grammatikalisch ausformulierten Sätzen erstellt; Skelette, Halbsätze und bloße Aufzählungen ersetzen keine Endfassung. Tabellen für tatsächlich parallele Angaben sind zulässig. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Markdown-Ausgabe steht ein nötiger Exporthinweis getrennt vom Empfängertext. Technische Prüfnotizen und Quellenprotokolle gehören nicht in den versandfertigen Text.

Kontrolliere vor Abschluss Produkt, Fakten, österreichische Rechtswahl, Quellenstatus, Zahlen, Fristen und tatsächlich gespeicherte Fassung. Eine technisch nicht ausgeführte Speicherung, Kalendereintragung, Buchung oder Übermittlung darf nicht als erledigt bezeichnet werden.

## 6. Beispiel

Heute 18 Minuten Telefonat zur Gewährleistungsforderung, abrechenbar in Phase H1. Erfrage nur noch die fehlende Person oder Quellenangabe.
