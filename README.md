# Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/release/atheile-ha/ha-release-notes-addon.svg)](https://github.com/atheile-ha/ha-release-notes-addon/releases)

Eine Web-Anwendung zur Verwaltung von Release Notes direkt in Home Assistant. Dokumentiere Änderungen, neue Features und bekannte Fehler übersichtlich.

## Features

### Release-Verwaltung
- Releases erstellen, bearbeiten und löschen
- Versionierung mit individuellen Release-Nummern
- Optionaler Release-Name (z.B. "Stable Release")
- Deutsches Datumsformat (DD.MM.YYYY)
- Expandierbare Release-Cards
- Kommentar-Feld für zusätzliche Informationen

### Kategorisierung
- **Neue Features** dokumentieren
- **Änderungen / Bugfixes** festhalten  
- **Bekannte Fehler** tracken
- 6 vordefinierte Kategorien: Allgemein, Heizung, Energie, Automation, Gerät, Integration
- Eigene Kategorien erstellen und verwalten
- Farbcodierte Badges

### Fehler-Management
- Automatische Übernahme offener Fehler in neue Releases
- Fehler als gelöst markieren mit Lösungsbeschreibung
- Historie gelöster Fehler bleibt sichtbar
- Gelöste Fehler können wieder geöffnet werden
- Gelöste Fehler erscheinen automatisch in den Änderungen

### Benutzerfreundlichkeit
- Suchfunktion über alle Releases
- Filter nach Kategorien
- Inline-Bearbeitung
- Responsive Design für Desktop & Mobile
- 100% offline (keine Internetverbindung erforderlich)
- Keine externen Abhängigkeiten

### Datensicherheit
- Automatisches Backup-System
- Persistente Speicherung in JSON
- Datenbank bleibt bei Updates erhalten

## Installation

### Via HACS (empfohlen)

1. HACS öffnen in Home Assistant
2. Klicke auf **⋮** (drei Punkte oben rechts)
3. Wähle **"Benutzerdefinierte Repositories"**
4. Füge hinzu:
   - **Repository:** `https://github.com/atheile-ha/ha-release-notes-addon`
   - **Kategorie:** `Integration`
5. Suche nach **"Release Notes Manager"**
6. Klicke **"Herunterladen"**
7. **Home Assistant neu starten**

### Konfiguration

Füge zu `configuration.yaml` hinzu:

```yaml
release_notes_manager:
```

Anschließend:
- **Home Assistant neu starten** (empfohlen)
- Oder: **YAML-Konfiguration neu laden**

### Zugriff

Öffne die Anwendung unter:
```
http://DEINE-HA-IP:8123/local/release-notes/release-notes.html
```

### Dashboard Integration

Füge eine iFrame-Karte hinzu:

```yaml
type: iframe
url: /local/release-notes/release-notes.html
aspect_ratio: 100%
```

Oder als eigenes Tab:

```yaml
views:
  - title: Release Notes
    path: releases
    icon: mdi:notebook
    cards:
      - type: iframe
        url: /local/release-notes/release-notes.html
        aspect_ratio: 100%
```

## Verwendung

### Erstes Release erstellen

1. Klicke **"+ Neues Release"**
2. Fülle aus:
   - **Version** (Pflicht): z.B. "2024.12.1"
   - **Name** (optional): z.B. "Weihnachts-Release"
   - **Datum**: Automatisch heutiges Datum
3. Füge **Features** hinzu unter "✨ Neue Features"
4. Füge **Änderungen** hinzu unter "🔄 Änderungen / Bugfixes"
5. Dokumentiere **Bekannte Fehler** unter "⚠️ Bekannte Fehler"
6. Klicke **"Speichern"**

### Bekannte Fehler verwalten

**Fehler hinzufügen:**
1. Release bearbeiten
2. Unter "⚠️ Bekannte Fehler" → "+ Hinzufügen"
3. Titel, Details und Kategorie eingeben
4. Speichern

**Fehler als gelöst markieren:**
1. Release bearbeiten
2. Bei Fehler auf "✓ Gelöst" klicken
3. Optional: Version und Lösungsbeschreibung
4. Klicke "Lösung dokumentieren"

**Resultat:**
- Fehler wird automatisch unter "🔄 Änderungen" angezeigt
- Fehler bleibt in Known Issues sichtbar mit Status "✓ Gelöst in X.X"
- Wird nicht mehr in neue Releases übernommen

**Fehler wieder öffnen:**
- Bei gelöstem Fehler auf "🔓 Wieder öffnen" klicken

### Automatische Fehler-Übernahme

Beim Erstellen eines neuen Releases:
- Alle offenen Fehler werden automatisch übernommen
- Gelöste Fehler werden nicht übernommen
- Hinweis: "ℹ️ X offene Fehler wurden automatisch übernommen"

### Kategorien verwalten

1. Klicke **"⚙ Kategorien"**
2. Neue Kategorie hinzufügen oder bestehende bearbeiten
3. Löschen mit "Löschen"-Button

### Suche & Filter

- **Suche:** Gib Suchbegriff ein - filtert alle Releases in Echtzeit
- **Filter:** Wähle Kategorie im Dropdown - zeigt nur Releases mit dieser Kategorie

## Release-Struktur

```
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

## Daten-Speicherung

**Speicherort:** `/config/www/release_data.json`  
**Backup:** `/config/www/release_data.json.backup`

Das Backup wird automatisch vor jedem Speichern erstellt.

## Troubleshooting

### Integration lädt nicht

1. Prüfe `configuration.yaml`: Ist `release_notes_manager:` vorhanden?
2. Prüfe Logs: **Einstellungen → System → Protokolle**
3. Suche nach: `release_notes_manager`

### Seite zeigt 404

1. Prüfe ob Datei existiert:
   ```bash
   ls /config/custom_components/release_notes_manager/www/release-notes.html
   ```
2. Home Assistant neu starten
3. Browser-Cache leeren: **Strg+Shift+R**

### Speichern funktioniert nicht

1. Prüfe Browser Console: **F12**
2. Prüfe Logs in Home Assistant
3. Prüfe Schreibrechte: `ls -la /config/www/`

### Daten nach Update weg

Daten sind im Backup:
```bash
cp /config/www/release_data.json.backup /config/www/release_data.json
```

Seite neu laden: **Strg+Shift+R**

### HACS zeigt Integration nicht

1. Repository URL korrekt?
2. Kategorie "Integration" gewählt?
3. HACS neu laden: **HACS → ⋮ → Repositories neu laden**

## Technische Details

**Anforderungen:**
- Home Assistant 2024.1.0 oder neuer
- Browser: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

**Performance:**
- Dateigröße: 26 KB (HTML)
- Ladezeit: < 100ms
- Empfohlen: Max. 100-200 Releases

**API Endpoints:**
```
GET  /local/release_data.json          # Daten laden
POST /api/release_notes_manager/save   # Daten speichern
```

**Technologie:**
- Backend: Python 3.11+, Async API (aiohttp)
- Frontend: Vanilla JavaScript (ES6+), Inline CSS
- Storage: JSON mit automatischem Backup
- Dependencies: Keine

## Changelog

### v0.3.1 (2024-12-16)
- **Fixed:** GitHub Actions Release Workflow
- **Enhanced:** HACS Metadata erweitert

### v0.3.0 (2024-12-16) - Initial Release
- Release-Verwaltung mit Versionierung
- Optionaler Release-Name
- Kategorisierte Features, Changes und Known Issues
- Automatische Übernahme offener Fehler
- Fehler als gelöst markieren mit Historie
- Gelöste Fehler in Changes-Sektion
- 6 vordefinierte Kategorien + eigene erstellen
- Deutsches Datumsformat (DD.MM.YYYY)
- Suchfunktion und Filter
- 100% Offline-Fähigkeit

## Support

- [GitHub Repository](https://github.com/atheile-ha/ha-release-notes-addon)
- [Issue Tracker](https://github.com/atheile-ha/ha-release-notes-addon/issues)
- [Discussions](https://github.com/atheile-ha/ha-release-notes-addon/discussions)

## Topics

[home-assistant](https://github.com/topics/home-assistant) · [hacs](https://github.com/topics/hacs) · [custom-integration](https://github.com/topics/custom-integration) · [release-notes](https://github.com/topics/release-notes)
