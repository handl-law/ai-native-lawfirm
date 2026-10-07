# 1. Paketregeln für die österreichische Adaption

Diese Datei gilt im gesamten Ordner ki-native-kanzlei-at. Die Format- und Ausformulierungsvorgaben der übergeordneten AGENTS.md/CLAUDE.md bleiben erhalten. Die dortigen deutschen Rechtsgrundlagen, BGB-Methodik, RVG-Hinweise, BRAO/BORA, deutschen Gerichtslisten und beA-Regeln gelten für dieses österreichische Paket nicht als sachliche Rechtsvorgabe. Verwende stattdessen die lokalen österreichischen Quellen und Workflows. Sonstige deutsche Pakete bleiben ausdrücklich unverändert deutsch.

## 1.1. Produkt und Rechtsstatus

Erstelle das konkret beauftragte vollständige Arbeitsprodukt. Keine Norm, Geschäftszahl, Zustellung, Rechtsmittelfrist, Steuerklassifikation oder Zeiterfassung erfinden. Version 0.1.0 ist keine behauptete fachliche Freigabe. Amtliche Grundlagen ersetzen nicht die Prüfung ihrer Anwendbarkeit im Mandat.

## 1.2. Lokale Werkzeuge

Nur die in diesem Paket vorhandenen Helfer verwenden. Fristenhelfer: bestätigte reguläre österreichische ZPO-/AVG-Profile ohne Sonderfälle. Journal: ausdrücklich bestätigte österreichische 20%-Inlandsumsätze, geprüfte Tarifpositionen manuell. Keine automatische ERV-, ebInterface-/UBL-, Kalender- oder Buchhaltungsintegration behaupten.

## 1.3. Test und Veröffentlichung

Führe `python3 tests/test_austria.py` und `python3 scripts/validate_package.py` aus. Teste bei Änderungen neue fachlich sinnvolle Grenzfälle. Nicht ausgeführte Modell-/Hosttests nicht als bestanden bezeichnen. Veröffentlichung erfolgt im autorisierten Fork; nichts an Klotzkettes Originalrepository pushen oder mergen.
