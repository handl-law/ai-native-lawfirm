# 1. Migration Deutschland → Österreich

Neufassung: handl-law, 7. Oktober 2026. Grundlage: Klotzkette/claude-fuer-deutsches-recht, Commit `1923e2aab44291fb93b34ae903630c625904ccd7`, deutsches Paket `ki-native-kanzlei` v445.33.4. Lokale Version: 0.1.0. Die 18 Workflows wurden neu geschrieben; Umfang, Volltext-Beispiele und Qualitätsnachweise des deutschen Originals werden nicht übernommen.

| Deutscher Ausgangspunkt | Österreichische Umsetzung |
| --- | --- |
| BRAO/BORA, deutsche Kammerregeln | RAO, aktuelle RL-BA, DSt und einschlägige österreichische Kammerregeln im konkreten Fall |
| RVG, deutsche Zeitaufstellungsurteile | Honorarvereinbarung, RATG und einschlägige aktuelle AHK; Kostenersatz gesondert |
| BGB und deutsches Verbraucherschutzrecht | ABGB, UGB, KSchG sowie einschlägiges österreichisches Sonderrecht |
| Deutsche ZPO/BGB-Kalenderprofile | Eigenständiger regulärer ZPO-/AVG-Helfer; sonstige Fristen manuell anhand konkreter Norm |
| bea-anlagen-vorbereiten | erv-beilagen-vorbereiten; keine Übermittlungsstellenintegration |
| 03_beA_Vorbereitung | 03_ERV_Vorbereitung |
| 19%-Inlandsrechnung | Nur ausdrücklich bestätigte österreichische Inlandsleistung mit 20 %; Sonderfälle werden abgewiesen |
| rvg-Tarifphase | tariff-Phase mit ausdrücklich geprüfter manueller RATG-/AHK-Position und Quellenangabe |
| Deutsches XRechnung-Skript | Nicht übernommen; österreichische ebInterface-/UBL-Anforderungen im Workflow, Export noch nicht implementiert |
| Deutsche Zitierweise und BGH-Anker | RIS, OGH, VfGH, VwGH; keine erfundenen österreichischen Entscheidungsanker |
| 24 deutsche Fachanwaltsakten | Nicht als österreichische Testakten übernommen |

## 1.1. Vorhandene Mandatsdaten

Benutze für die österreichischen Helfer einen neuen Mandatsordner. Ein deutsches SQLite-Journal wird nicht automatisch migriert. Bestätigte Angaben nur nach Prüfung von Honorar, Steuer und Quellen übernehmen; deutsche 19%-Phasen und rvg-IDs sind nicht einfach umzubenennen.

## 1.2. Fachliche Prüfung vor Freigabe

Die Normgrundlagen im Quellenprotokoll wurden abgerufen; das ist keine Prüfung sämtlicher Mandatskonstellationen. Offene vertiefte Prüfungen betreffen insbesondere aktuelle RL-BA/AHK- und Kammer-/Treuhandfassungen, Gebührenbewertungen, Verfahrenssonderfälle, Rechtsmittelfristen, ERV-Zustellung und technische Empfängervorgaben. Fallbezogene Quellenprüfung ist in jedem Skill verbindlich. Automatischer ERV-Versand, österreichischer XML-Rechnungsexport und Calendar-/Kanzleisoftwareanschlüsse sind nicht implementiert.
