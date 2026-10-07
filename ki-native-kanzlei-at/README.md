# 1. KI-native Kanzlei Österreich

Österreichische Adaption für **handl-law** auf Grundlage von [Klotzkettes KI-native Kanzlei](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/ki-native-kanzlei). Version **0.1.0**, 7. Oktober 2026. Achtzehn kompaktere, neu geschriebene Workflows; kein Anspruch auf Übernahme des Umfangs oder der fachlichen Qualitätsnachweise des deutschen Originals.

## 1.1. Enthaltene Workflows

Mandatssteuerung, Annahme/Kollision, Akte/Fristen, Fristenberechnung, Anwaltsberufsrecht, Geldwäsche, Honorar/Budget, tatsächliche Zeit, Übergabe, Recherche, Schriftsätze, AGB-Prüfung, Vertragsgestaltung, Mandantenkommunikation, ERV/Beilagen, Honorarnote/E-Rechnung, Zahlungen/Buchhaltung und Abschluss. Die österreichische ERV-Funktion heißt `erv-beilagen-vorbereiten`; sie ersetzt im AT-Paket `bea-anlagen-vorbereiten`.

## 1.2. Direkt anfangen

„Bearbeite mein österreichisches Mandat im bezeichneten Ordner. Erstelle zuerst den verlangten Entwurf. Führe bestätigte Honorargrundlage und tatsächliche Zeit mit; prüfe Zustellung, Fristen und österreichische Quellen vor Verwendung.“

Alternativ den [Standalone-Schnellstart](ki-native-kanzlei-at-schnellstart.md) als Arbeitsanweisung verwenden. Dieser Text installiert keinen Helfer und erteilt keinen zusätzlichen Dateizugriff.

## 1.3. Installieren und ausführen

Dieses Verzeichnis ist ein selbständiges Agent-Plugins-1.0-Paket mit root plugin.json und skills/. Importiere das ZIP über den im Konto tatsächlich verfügbaren Plugin-Import; eine bestimmte Freischaltung oder Hostkompatibilität wird nicht zugesichert. Im Repository ist das Paket zusätzlich im Marketplace registriert. Für Claude Code kann der Checkout als lokaler Marketplace hinzugefügt und ausschließlich `ki-native-kanzlei-at` installiert werden. Alle anderen Pakete im Fork bleiben deutsches Recht.

Die lokalen Python-Helfer benötigen echten Dateizugriff und Python 3.10 oder neuer. [Journal und Zeiterfassung](references/mandatsordner-und-cli.md) · [Fristenhilfe](references/fristen-rechenhilfe.md) · [Zitierweise](references/zitierweise.md) · [Quellen und Prüfstatus](references/rechtsquellen.md) · [Migrationsentscheidungen](MIGRATION.md).

## 1.4. Implementierter Umfang und offene Anschlüsse

Das Journal unterstützt bestätigte österreichische 20%-Inlandsumsätze, Zeithonorar, Pauschale, Deckel, Schätzung und zuvor geprüfte manuelle Tarifpositionen. Der Fristenhelfer unterstützt ausschließlich bestätigte reguläre österreichische ZPO-/AVG-Profile ohne Sonderfälle. ERV und elektronische Rechnungen sind fachliche Vorbereitungsworkflows: keine Einreichungs-API, kein ebInterface-/UBL-Exporter, kein automatischer Kalender und keine Kanzleisoftware-/handl.law-Verbindung. Deutsche Skripte, Kalenderbeispiele und 24 deutsche Fachanwaltsakten sind nicht Teil dieses Pakets.

## 1.5. Validierung und fachlicher Status

```bash
python3 tests/test_austria.py
python3 scripts/validate_package.py
```

Technische Tests prüfen die tatsächlich implementierten lokalen Helfer und Paketstruktur. Sie zertifizieren keine fachliche Rechtsprüfung sämtlicher Workflows und keine Nutzung in einem bestimmten Host. Der dokumentierte Quellenabruf ist von der Prüfung der fallbezogenen Anwendbarkeit zu unterscheiden. Eine österreichische fachliche Durchsicht und die im [Migrationsplan](MIGRATION.md) benannten Quellen-/Integrationsprüfungen stehen noch aus.

## 1.6. Herkunft und Lizenz

Grundlage: upstream Commit `1923e2aab44291fb93b34ae903630c625904ccd7`. Ursprüngliche Klotzkette-/Anthropic-Attribution bleibt erhalten, ebenso die Wahl zwischen Apache-2.0 und MIT. Die neuen österreichischen Workflowtexte und Änderungen sind als handl-law-Adaption bezeichnet. Siehe NOTICE, LICENSE-APACHE und LICENSE-MIT.
