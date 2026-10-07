---
name: fristen-berechnen-ueberwachen
description: "Prüft österreichische Verfahrens- oder materielle Fristen, Zustellung, Berechnung, Kontrollverantwortung und tatsächliche Kalenderübernahme."
---

# Österreichische Fristen prüfen

Österreichische Neufassung für handl-law, 7. Oktober 2026, auf Grundlage der Workflow-Struktur von Klotzkette. Version 0.2.0; Data-&-Technology-Anschluss ergänzt, keine behauptete fachliche Freigabe.

## 1. Zweck und Anwendungsfall

Prüft österreichische Verfahrens- oder materielle Fristen, Zustellung, Berechnung, Kontrollverantwortung und tatsächliche Kalenderübernahme. Lies vor der Bearbeitung [Arbeitsweise](../../references/arbeitsweise.md). Österreichische Sach-, Verfahrens- und Berufsregeln gehen deutschen Vorlagen aus dem Quellrepository vor. Bei Auslandsbezug ist die Rechtswahl gesondert zu bestimmen.

## 2. Eingaben

Verfahrensart, Entscheidung, Rechtsmittelbelehrung, Zustellnachweis, Fristnorm, Rechtsstand, Kalenderort und Vertretung. Lies vorhandene Unterlagen zuerst und übernimm bereits bestätigte Antworten. Stelle nur Rückfragen, deren Antwort das konkrete Ergebnis verändert. Fehlende Tatsachen bleiben ausdrücklich offen.

## 3. Ablauf / Checkliste

### 3.0. Data-&-Technology-Anschluss

Bei einem Auftrag aus der Data-&-Technology-Praxis nutze den [Praxisrouter](../data-technology-steuern/SKILL.md) und die konkret passende Vertiefung: [cyber-incident-tech](../cyber-incident-tech/SKILL.md), [datenschutz-verfahren-tech](../datenschutz-verfahren-tech/SKILL.md). Ereignisbezogene Meldepflichten mit Stunden-/Kenntnistrigger und Zeitzone sind keine regulären Tagesfristen und werden nicht durch fristen_at.py berechnet. EU-Sachrecht bleibt der europäische Kern; österreichische Umsetzung, Verfahren, Behörden und Vertragsrecht ergänzen. Beauftragt relevante Regeln anwenden und das konkrete Produkt fertigstellen, statt alle Fachgebiete auf Vorrat zu prüfen.

### 3.1. Bearbeitungsschritt

Bestimme erst das konkrete Verfahren und die Spezialnorm. Österreichische ZPO, AVG/VwGVG, BAO, StPO, AußStrG und materielles Recht sind keine austauschbaren Fristenregime. Prüfe Rechtsmittel, Länge, Verlängerbarkeit und Übergangsrecht.

### 3.2. Bearbeitungsschritt

Prüfe tatsächliche Wirksamkeit und Zeitpunkt der Zustellung nach ZustG und einschlägigen ERV-Regeln. Entscheidungsdatum, Downloadzeitpunkt und E-Mail-Datum sind keine automatische Zustellfiktion; lese insbesondere den Originalnachweis.

### 3.3. Bearbeitungsschritt

Bei regulären ZPO-Fristen prüfe §§ 125 und 126 ZPO; bei anwendbarem AVG §§ 32 und 33 AVG. Bei Tagesfristen wird der auslösende Tag nicht mitgezählt; Wochen-/Monats-/Jahresfristen sind kalenderbezogen zu berechnen.

### 3.4. Bearbeitungsschritt

Prüfe die Endverschiebung im zutreffenden Regime. § 126 ZPO erfasst neben Wochenende und Feiertagen auch Karfreitag; § 33 AVG erfasst außerdem 24. Dezember. Übertrage dies nicht ungeprüft auf materielle oder besondere Verfahrensfristen.

### 3.5. Bearbeitungsschritt

Prüfe Unterbrechung, Hemmung, verhandlungsfreie Zeiten, Spezialregeln und den maßgeblichen vollständigen Feiertagskalender. Postlauf, elektronisches Einlangen und rechtzeitiger Übermittlungsweg benötigen eine separate rechtliche Prüfung.

### 3.6. Bearbeitungsschritt

Der optionale scripts/fristen_at.py rechnet nur bestätigte reguläre ZPO-/AVG-Profile ohne Sonderfälle. Er bestimmt weder Zustellung noch Fristlänge noch Anwendbarkeit und lehnt unbestätigte Profile ab. Für andere Regime erstelle einen manuell belegten Vermerk.

### 3.7. Bearbeitungsschritt

Kontrolliere die Rechnung unabhängig, bestimme Vorfrist und Vertretung und dokumentiere tatsächliche Kalenderspeicherung. Schließe erst nach geprüftem Einlangens- oder sonst erforderlichem Erledigungsbeleg.

## 4. Quellenpflicht

Es gelten die österreichische [Zitierweise](../../references/zitierweise.md) und der [Quellenplan](../../references/rechtsquellen.md). Prüfe den vollständigen Norm- oder Entscheidungstext zum maßgeblichen Zeitpunkt. Keine Geschäftszahl, RS-Nummer, Randziffer oder Literaturfundstelle aus bloßem Modellwissen. Ein Link oder Suchtreffer ist noch kein Beleg seiner rechtlichen Anwendung; fehlender Zugriff bleibt als konkreter Prüfbedarf sichtbar.

## 5. Ausgabeformat

Vollständig begründeter Fristenvermerk mit Rechtswahl, Zustellbeleg, Rechenweg, Sondertagen, Kontrollperson und Kalenderstatus. Das Endprodukt wird vollständig in grammatikalisch ausformulierten Sätzen erstellt; Skelette, Halbsätze und bloße Aufzählungen ersetzen keine Endfassung. Tabellen für tatsächlich parallele Angaben sind zulässig. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Markdown-Ausgabe steht ein nötiger Exporthinweis getrennt vom Empfängertext. Technische Prüfnotizen und Quellenprotokolle gehören nicht in den versandfertigen Text.

Kontrolliere vor Abschluss Produkt, Fakten, österreichische Rechtswahl, Quellenstatus, Zahlen, Fristen und tatsächlich gespeicherte Fassung. Eine technisch nicht ausgeführte Speicherung, Kalendereintragung, Buchung oder Übermittlung darf nicht als erledigt bezeichnet werden.

## 6. Beispiel

Prüfe eine zweiwöchige Frist, deren rechnerisches Ende auf den 24. Dezember fällt. Vergleiche nur nach bestätigter Rechtswahl ZPO- und AVG-Regime.
