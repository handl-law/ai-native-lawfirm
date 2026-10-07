---
name: abrechnung-e-rechnung
description: "Erstellt österreichische Honorarnotenentwürfe und prüft den erforderlichen elektronischen Rechnungsweg; erzeugt keinen behaupteten validierten XML-Export."
---

# Honorarnote und E-Rechnung vorbereiten

Österreichische Neufassung für handl-law, 7. Oktober 2026, auf Grundlage der Workflow-Struktur von Klotzkette. Version 0.2.0; Data-&-Technology-Anschluss ergänzt, keine behauptete fachliche Freigabe.

## 1. Zweck und Anwendungsfall

Erstellt österreichische Honorarnotenentwürfe und prüft den erforderlichen elektronischen Rechnungsweg; erzeugt keinen behaupteten validierten XML-Export. Lies vor der Bearbeitung [Arbeitsweise](../../references/arbeitsweise.md). Österreichische Sach-, Verfahrens- und Berufsregeln gehen deutschen Vorlagen aus dem Quellrepository vor. Bei Auslandsbezug ist die Rechtswahl gesondert zu bestimmen.

## 2. Eingaben

Honorarvereinbarung, bestätigte Leistung, Tarifprüfung, Auslagen, Zahlungen, Rechnungsparteien, UID, Steuerstatus und Empfängeranforderungen. Lies vorhandene Unterlagen zuerst und übernimm bereits bestätigte Antworten. Stelle nur Rückfragen, deren Antwort das konkrete Ergebnis verändert. Fehlende Tatsachen bleiben ausdrücklich offen.

## 3. Ablauf / Checkliste

### 3.0. Data-&-Technology-Anschluss

Bei einem Auftrag aus der Data-&-Technology-Praxis nutze den [Praxisrouter](../data-technology-steuern/SKILL.md) und die konkret passende Vertiefung: [data-technology-steuern](../data-technology-steuern/SKILL.md). EU-Sachrecht bleibt der europäische Kern; österreichische Umsetzung, Verfahren, Behörden und Vertragsrecht ergänzen. Beauftragt relevante Regeln anwenden und das konkrete Produkt fertigstellen, statt alle Fachgebiete auf Vorrat zu prüfen.

### 3.1. Bearbeitungsschritt

Gleiche bestätigte Leistungen mit Honorarphase und Auftrag ab. Zeithonorar basiert auf tatsächlichen Minuten, Pauschale auf Vereinbarung und Fälligkeit, Tarifposition auf geprüfter RATG-/AHK-Berechnung.

### 3.2. Bearbeitungsschritt

Trenne Mandantenhonorar, gerichtliche Kostennote, Auslagen, durchlaufende Posten, Vorschüsse und Fremdgeld. Eine bekannte Zahlung darf nicht ungeprüft vom Bruttobetrag abgezogen werden.

### 3.3. Bearbeitungsschritt

Prüfe Rechnungsangaben nach § 11 UStG 1994, insbesondere Parteien, Leistung/Zeitraum, Entgelt, steuerliche Angaben und erforderliche Nummer/UID. Prüfe Leistungsort, Befreiung oder Reverse Charge vor Steuerausweis.

### 3.4. Bearbeitungsschritt

Nutze den lokalen Journalentwurf nur für bestätigte österreichische Inlandsumsätze mit 20 %. Er weist keine Rechnungsnummer zu und setzt invoice_ready immer auf false; rechnerische Vollständigkeit ist keine steuerrechtliche Freigabe.

### 3.5. Bearbeitungsschritt

Bestimme Empfänger und erforderliches Format. Bei öffentlicher Verwaltung prüfe e-Rechnung.gv.at und aktuelle ebInterface-/UBL-Anforderungen einschließlich Auftragsreferenz; eine PDF-Rechnung ist nicht automatisch eine strukturierte Rechnung.

### 3.6. Bearbeitungsschritt

Dieses Paket liefert Markdown/JSON-Entwürfe, keinen ebInterface-/UBL-Exporter. Verwende für tatsächliche XML-Erzeugung ein verfügbares geprüftes Werkzeug und dokumentiere Schema- und Empfängervalidierung. Ohne Werkzeug bleibt der Export als offen bezeichnet.

### 3.7. Bearbeitungsschritt

Erstelle die vollständig ausformulierte Honorarnote und den separaten Prüfvermerk. Ausstellung, Buchhaltung und Versand erfolgen nur mit entsprechendem Auftrag und tatsächlich vorhandener Integration.

## 4. Quellenpflicht

Es gelten die österreichische [Zitierweise](../../references/zitierweise.md) und der [Quellenplan](../../references/rechtsquellen.md). Prüfe den vollständigen Norm- oder Entscheidungstext zum maßgeblichen Zeitpunkt. Keine Geschäftszahl, RS-Nummer, Randziffer oder Literaturfundstelle aus bloßem Modellwissen. Ein Link oder Suchtreffer ist noch kein Beleg seiner rechtlichen Anwendung; fehlender Zugriff bleibt als konkreter Prüfbedarf sichtbar.

## 5. Ausgabeformat

Ausformulierter Honorarnotenentwurf, nachvollziehbare Berechnung und konkret benannter Rechnungs-/Exportstatus. Das Endprodukt wird vollständig in grammatikalisch ausformulierten Sätzen erstellt; Skelette, Halbsätze und bloße Aufzählungen ersetzen keine Endfassung. Tabellen für tatsächlich parallele Angaben sind zulässig. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Markdown-Ausgabe steht ein nötiger Exporthinweis getrennt vom Empfängertext. Technische Prüfnotizen und Quellenprotokolle gehören nicht in den versandfertigen Text.

Kontrolliere vor Abschluss Produkt, Fakten, österreichische Rechtswahl, Quellenstatus, Zahlen, Fristen und tatsächlich gespeicherte Fassung. Eine technisch nicht ausgeführte Speicherung, Kalendereintragung, Buchung oder Übermittlung darf nicht als erledigt bezeichnet werden.

## 6. Beispiel

Bereite eine Honorarnote über 18 Minuten zu 240 EUR netto je Stunde vor. Prüfe den bestätigten Steuerstatus und die besonderen Empfängerfelder, falls der Bund Rechnungsempfänger ist.
