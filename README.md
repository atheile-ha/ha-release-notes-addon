# Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/release/your-username/ha-release-notes-manager.svg)](https://github.com/your-username/ha-release-notes-manager/releases)
[![License](https://img.shields.io/github/license/your-username/ha-release-notes-manager.svg)](LICENSE)

Eine intuitive Web-Anwendung zur Verwaltung von Release Notes direkt in Home Assistant. Dokumentiere Änderungen, neue Features und bekannte Fehler professionell und übersichtlich.

![Release Notes Manager Screenshot](docs/screenshot.png)

## 📋 Inhaltsverzeichnis

- [Features](#-features)
- [Installation](#-installation)
  - [HACS (empfohlen)](#hacs-empfohlen)
  - [Manuelle Installation](#manuelle-installation)
- [Konfiguration](#️-konfiguration)
- [Verwendung](#-verwendung)
- [Funktionen im Detail](#-funktionen-im-detail)
- [Troubleshooting](#-troubleshooting)
- [Technische Details](#-technische-details)
- [Changelog](#-changelog)
- [Support](#-support)

## ✨ Features

### Release-Verwaltung
- ✅ **Releases erstellen, bearbeiten und löschen**
- ✅ **Optionaler Release-Name** (z.B. "Stable Release")
- ✅ **Versionierung** mit individuellen Release-Nummern

### Kategorisierung
- ✅ **Neue Features** dokumentieren
- ✅ **Änderungen / Bugfixes** festhalten
- ✅ **Bekannte Fehler** tracken
- ✅ **6 vordefinierte Kategorien**: Allgemein, Heizung, Energie, Automation, Gerät, Integration
- ✅ **Eigene Kategorien** erstellen und verwalten
- ✅ **Farbcodierte Badges** für bessere Übersicht

### Fehler-Management
- ✅ **Automatische Übernahme** offener Fehler in neue Releases
- ✅ **Fehler als gelöst markieren** mit Lösungsbeschreibung
- ✅ **Historie gelöster Fehler** bleibt sichtbar
- ✅ **Gelöste Fehler wieder öffnen** bei Bedarf
- ✅ **Gelöste Fehler erscheinen automatisch** in den Änderungen

### Benutzerfreundlichkeit
- ✅ **Suchfunktion** über alle Releases
- ✅ **Filter nach Kategorien**
- ✅ **Expandierbare Release-Cards**
- ✅ **Inline-Bearbeitung**
- ✅ **Responsive Design** für Desktop & Mobile
- ✅ **Keine Internetverbindung** erforderlich (100% offline)
- ✅ **Keine externen Abhängigkeiten**

### Datensicherheit
- ✅ **Automatisches Backup-System**
- ✅ **Persistente Speicherung** in JSON
- ✅ **Keine Auth-Tokens** erforderlich
- ✅ **Datenbank bleibt** bei Updates erhalten

## 📥 Installation

### HACS (empfohlen)

1. **HACS öffnen** in Home Assistant
2. **Integration hinzufügen**:
   - Klicke auf die drei Punkte ⋮ oben rechts
   - Wähle "Benutzerdefinierte Repositories"
3. **Repository hinzufügen**:
   - URL: `https://github.com/your-username/ha-release-notes-manager`
   - Kategorie: `Integration`
   - Klicke "Hinzufügen"
4. **Integration installieren**:
   - Suche nach "Release Notes Manager"
   - Klicke "Herunterladen"
   - Warte bis Download abgeschlossen
5. **Home Assistant neu starten**

### Manuelle Installation

1. **Download**: Lade die neueste Version von [Releases](https://github.com/your-username/ha-release-notes-manager/releases)
2. **Entpacken**: Extrahiere das Archiv
3. **Kopieren**: 
   ```bash
   # Kopiere den Ordner nach:
   /config/custom_components/release_notes_manager/
   ```
4. **Struktur prüfen**:
   ```
   /config/custom_components/release_notes_manager/
   ├── __init__.py
   ├── manifest.json
   ├── api.py
   └── www/
       └── index.html
   ```
5. **Home Assistant neu starten**

## ⚙️ Konfiguration

### Schritt 1: Integration aktivieren

Füge folgendes zu deiner `configuration.yaml` hinzu:

```yaml
release_notes_manager:
```

### Schritt 2: Konfiguration neu laden

**WICHTIG**: Nach dem Hinzufügen zur `configuration.yaml`:

**Option A - Neustart (empfohlen bei Erstinstallation):**
- Einstellungen → System → Neu starten
- Warte bis Home Assistant vollständig neu gestartet ist

**Option B - Konfiguration neu laden (bei Updates):**
- Einstellungen → System → YAML-Konfiguration neu laden
- Wähle "Alle YAML-Konfigurationen neu laden"

### Schritt 3: Integration prüfen

Prüfe in den Logs ob die Integration geladen wurde:

```
Einstellungen → System → Protokolle
```

Suche nach: `release_notes_manager`

Du solltest sehen:
```
✅ Release Notes Manager initialized
✅ Release Notes API registered
✅ Static files registered at /local/release-notes/
```

### Schritt 4: Zugriff

Öffne die Anwendung:
```
http://DEINE-HA-IP:8123/local/release-notes/release-notes.html
```

Oder als iFrame in Lovelace Dashboard (siehe unten).

## 🎯 Verwendung

### Dashboard Integration (Lovelace)

Füge eine Webseiten-Karte hinzu:

```yaml
type: iframe
url: /local/release-notes/release-notes.html
aspect_ratio: 100%
```

Oder im YAML-Modus:

```yaml
views:
  - title: Release Notes
    path: releases
    cards:
      - type: iframe
        url: /local/release-notes/release-notes.html
        aspect_ratio: 100%
```

### Erstes Release erstellen

1. **Klicke** auf "+ Neues Release"
2. **Fülle aus**:
   - **Version*** (Pflichtfeld): z.B. "2024.12.1"
   - **Name** (optional): z.B. "Weihnachts-Release"
   - **Datum**: Automatisch heutiges Datum
3. **Füge Features hinzu**:
   - Klicke "+ Hinzufügen" unter "✨ Neue Features"
   - Titel: "Neue Heizungssteuerung"
   - Kategorie: "Heizung"
   - Details: "PWM-basierte Fußbodenheizung implementiert"
4. **Füge Änderungen hinzu**:
   - Klicke "+ Hinzufügen" unter "🔄 Änderungen / Bugfixes"
   - Titel: "Dashboard-Layout optimiert"
5. **Speichere**: Klicke "Speichern"

### Bekannte Fehler verwalten

#### Fehler hinzufügen
1. Release bearbeiten
2. Unter "⚠️ Bekannte Fehler" → "+ Hinzufügen"
3. Titel: "Automation verzögert"
4. Details: "Morgen-Routine startet 5 Min zu spät"
5. Kategorie: "Automation"
6. Speichern

#### Fehler als gelöst markieren
1. Release bearbeiten
2. Bei Fehler auf "✓ Gelöst" klicken
3. Version: "2024.12.2" (optional)
4. Lösung: "Zeitzone-Offset korrigiert"
5. "Lösung dokumentieren"

**Resultat:**
- ✅ Fehler wird automatisch unter "🔄 Änderungen" angezeigt
- ✅ Fehler bleibt in Known Issues mit "✓ Gelöst in X.X"
- ✅ Wird NICHT mehr in neue Releases übernommen

#### Automatische Fehler-Übernahme

Wenn du ein **neues Release** erstellst:
- ✅ Alle **offenen Fehler** werden automatisch übernommen
- ✅ **Gelöste Fehler** werden NICHT übernommen
- ✅ Du siehst einen Hinweis: "ℹ️ X offene Fehler wurden automatisch übernommen"

### Kategorien verwalten

1. Klicke "⚙ Kategorien"
2. **Neue Kategorie**:
   - Name: "Security"
   - Enter oder "+ Hinzufügen"
3. **Kategorie bearbeiten**:
   - Klicke "Bearbeiten"
   - Ändere Namen
   - "Speichern"
4. **Kategorie löschen**:
   - Klicke "Löschen"
   - Bestätige

### Suche & Filter

**Suche:**
- Gib Suchbegriff ein (z.B. "Heizung")
- Filtert alle Releases in Echtzeit

**Filter:**
- Wähle Kategorie im Dropdown
- Zeigt nur Releases mit dieser Kategorie

## 🔧 Funktionen im Detail

### Release-Struktur

Jedes Release kann enthalten:

```yaml
Version: 2024.12.1
Name: Weihnachts-Release (optional)
Datum: 15.12.2024

✨ Neue Features:
  - [Heizung] PWM-Steuerung implementiert
    Details: Genauere Temperaturregelung

🔄 Änderungen / Bugfixes:
  - [Automation] Dashboard optimiert
  - 🐛 Gelöst in 2024.12.1: Timing-Problem
    Lösung: Zeitzone-Offset korrigiert

⚠️ Bekannte Fehler:
  - [Energie] Zählerstand manchmal ungenau
  - ✓ Gelöst in 2024.12.2: Automation verzögert

💬 Kommentare:
  Wichtiges Release mit vielen Verbesserungen
```

### Daten-Speicherung

**Speicherort:**
```
/config/www/release_data.json
```

**Backup:**
```
/config/www/release_data.json.backup
```

**Format:**
```json
{
  "releases": [...],
  "knownIssues": [...],
  "categories": [...],
  "lastUpdate": "2024-12-16T12:00:00.000Z"
}
```

### Fehler-Workflow

```
1. Fehler erfassen
   ↓
2. In neue Releases übernehmen (automatisch)
   ↓
3. Fehler beheben
   ↓
4. Als gelöst markieren
   ↓
5. Erscheint in Änderungen
   ↓
6. Bleibt in Historie sichtbar
   ↓
7. Wird nicht mehr übernommen
```

## 🔍 Troubleshooting

### Integration lädt nicht

**Problem:** Integration erscheint nicht nach Neustart

**Lösung:**
1. Prüfe `configuration.yaml`:
   ```yaml
   release_notes_manager:  # ← Richtig geschrieben?
   ```
2. Prüfe Logs:
   ```
   Einstellungen → System → Protokolle
   ```
3. Prüfe Struktur:
   ```bash
   ls -la /config/custom_components/release_notes_manager/
   # Sollte zeigen: __init__.py, manifest.json, api.py, www/
   ```

### Seite zeigt Fehler 404

**Problem:** `/local/release-notes/index.html` nicht gefunden

**Lösung:**
1. Prüfe ob Datei existiert:
   ```bash
   ls -la /config/custom_components/release_notes_manager/www/index.html
   ```
2. Neustart Home Assistant
3. Browser-Cache leeren (Strg+Shift+R)

### Speichern funktioniert nicht

**Problem:** "Speichern fehlgeschlagen"

**Lösung:**
1. Prüfe Browser Console (F12):
   ```javascript
   // Sollte zeigen:
   POST /api/release_notes_manager/save
   ```
2. Prüfe Logs in HA
3. Prüfe Schreibrechte:
   ```bash
   ls -la /config/www/
   # release_data.json sollte existieren
   ```

### Daten verschwinden nach Update

**Problem:** Nach Integration-Update sind Daten weg

**Lösung:**
```bash
# Daten sind im Backup:
cp /config/www/release_data.json.backup /config/www/release_data.json

# Seite neu laden (Strg+Shift+R)
```

### HACS zeigt Integration nicht

**Problem:** Integration nicht in HACS sichtbar

**Lösung:**
1. Repository URL korrekt?
2. Kategorie "Integration" gewählt?
3. HACS neu laden:
   ```
   HACS → ⋮ → Repositories neu laden
   ```

## 📊 Technische Details

### Anforderungen

- **Home Assistant:** 2024.1.0 oder neuer
- **Browser:** Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Internetverbindung:** Nicht erforderlich
- **Externe Dependencies:** Keine

### Technologie-Stack

**Backend:**
- Python 3.11+
- Home Assistant Core Integration
- Async API (aiohttp)
- JSON Storage
- Automatic Backup

**Frontend:**
- Vanilla JavaScript (ES6+)
- Inline CSS (Tailwind-inspiriert)
- Keine externen Libraries
- 26 KB komprimiert

### Performance

- **Dateigröße:** 26 KB (HTML)
- **Ladezeit:** < 100ms
- **Memory:** < 2 MB
- **Empfohlen:** Max. 100-200 Releases
- **Maximum:** ~1000 Releases technisch möglich

### API Endpoints

```
GET  /local/release_data.json          # Daten laden
POST /api/release_notes_manager/save   # Daten speichern (ohne Auth)
```

### Sicherheit

- ✅ XSS Protection (HTML Escaping)
- ✅ No eval() usage
- ✅ CSP compatible
- ✅ No external requests
- ✅ Local data only
- ❌ Keine Auth erforderlich (lokaler Zugriff)

## 📝 Changelog

### v0.3.0 (2024-12-16) - Initial Release

**Features:**
- ✨ Release-Verwaltung mit Versionierung
- ✨ Optionaler Release-Name
- ✨ Kategorisierte Features, Changes und Known Issues
- ✨ Automatische Übernahme offener Fehler
- ✨ Fehler als gelöst markieren mit Historie
- ✨ Gelöste Fehler in Changes-Sektion
- ✨ 6 vordefinierte Kategorien + eigene erstellen
- ✨ Deutsches Datumsformat (DD.MM.YYYY)
- ✨ Suchfunktion über alle Releases
- ✨ Filter nach Kategorien
- ✨ Expandierbare Release-Cards
- ✨ Responsive Design
- ✨ 100% Offline-Fähigkeit

**Technical:**
- ✨ Vanilla JavaScript (keine Dependencies)
- ✨ Automatisches Backup-System
- ✨ Persistente JSON-Speicherung

## 💬 Support

### Dokumentation
- [GitHub Repository](https://github.com/your-username/ha-release-notes-manager)
- [Issue Tracker](https://github.com/your-username/ha-release-notes-manager/issues)
- [Discussions](https://github.com/your-username/ha-release-notes-manager/discussions)

### Hilfe erhalten

1. **Prüfe** [Troubleshooting](#-troubleshooting)
2. **Suche** in [Issues](https://github.com/your-username/ha-release-notes-manager/issues)
3. **Erstelle** ein neues Issue mit:
   - Home Assistant Version
   - Browser & Version
   - Fehlerbeschreibung
   - Logs (aus HA & Browser Console)

---

**Entwickelt mit ❤️ für die Home Assistant Community**

[⬆️ Zurück nach oben](#home-assistant-release-notes-manager)
