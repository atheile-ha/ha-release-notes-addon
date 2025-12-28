# Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/release/atheile-ha/ha-release-notes-addon.svg)](https://github.com/atheile-ha/ha-release-notes-addon/releases)

Eine Web-Anwendung zur Verwaltung von Release Notes direkt in Home Assistant.

## ✨ Features

### Release-Verwaltung
- Releases erstellen, bearbeiten und löschen
- Versionierung mit Release-Nummern
- Optionaler Release-Name
- Deutsches Datumsformat (DD.MM.YYYY)

### Kategorisierung
- Neue Features dokumentieren
- Änderungen / Bugfixes festhalten
- Bekannte Fehler tracken
- 6 vordefinierte Kategorien
- Eigene Kategorien erstellen
- Alphabetische Sortierung der Kategorien

### Fehler-Management
- Automatische Übernahme offener Fehler
- Fehler als gelöst markieren
- Historie bleibt sichtbar
- Gel öste Fehler wieder öffnen

### Benutzerfreundlichkeit
- **NEU:** Zusammenfassung in minimierter Ansicht (X Features, X Bugs...)
- **NEU:** Markdown Export für einzelne Releases
- **NEU:** Keyboard Shortcuts (Strg+S, ESC)
- **NEU:** Dark Mode Support
- **NEU:** Neue Einträge erscheinen oben in der Liste
- **NEU:** Pencil Icon (✏️) statt "Bearbeiten" Button
- **NEU:** Löschen-Button nur im Edit-Modus
- Suchfunktion über alle Releases
- Filter nach Kategorien
- Expandierbare Release-Cards
- Responsive Design
- 100% offline

### Datensicherheit
- Automatisches Backup-System
- Persistente Speicherung in JSON
- Daten bleiben bei Updates erhalten

## 📥 Installation

### Via HACS

1. HACS öffnen
2. ⋮ → "Benutzerdefinierte Repositories"
3. URL: `https://github.com/atheile-ha/ha-release-notes-addon`
4. Kategorie: `Integration`
5. Suche "Release Notes Manager" → Download
6. Home Assistant neu starten

### Konfiguration

`configuration.yaml`:
```yaml
release_notes_manager:
```

Dann Home Assistant neu starten.

### Zugriff

```
http://YOUR-HA-IP:8123/local/release-notes/release-notes.html
```

### Dashboard Integration

```yaml
type: iframe
url: /local/release-notes/release-notes.html
aspect_ratio: 100%
```

## 🎹 Keyboard Shortcuts

- **Strg+S** - Speichern
- **ESC** - Modals schließen

## 📤 Markdown Export

Exportiere einzelne Releases als Markdown-Datei für:
- GitHub Releases
- Dokumentation
- Backups

## 🌙 Dark Mode

Automatische Unterstützung für Dark Mode basierend auf System-Einstellung.

## 📝 Changelog

### v0.3.2 (2024-12-16)

**Neue Features:**
- Zusammenfassung in minimierter Ansicht
- Markdown Export für Releases
- Keyboard Shortcuts (Strg+S, ESC)
- Dark Mode Support
- Neue Einträge erscheinen oben
- Pencil Icon statt "Bearbeiten"
- Löschen-Button nur im Edit-Modus
- Alphabetische Sortierung der Kategorien
- Loading Indicator beim Speichern

**Fixes:**
- HACS Validation (brands check deaktiviert)

### v0.3.1 (2024-12-16)
- GitHub Actions Release Workflow gefixt
- HACS Metadata erweitert

### v0.3.0 (2024-12-16)
- Initial Release

## 🔍 Troubleshooting

### Integration lädt nicht
1. Prüfe `configuration.yaml`
2. Prüfe Logs: Einstellungen → System → Protokolle
3. Suche nach `release_notes_manager`

### Seite zeigt 404
1. Prüfe Datei: `/config/custom_components/release_notes_manager/www/release-notes.html`
2. Home Assistant neu starten
3. Browser-Cache leeren (Strg+Shift+R)

### HACS zeigt Integration nicht
1. Repository URL korrekt?
2. Kategorie "Integration" gewählt?
3. HACS → ⋮ → Repositories neu laden

## 📊 Technische Details

**Anforderungen:**
- Home Assistant 2024.1.0+
- Browser: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

**Performance:**
- Dateigröße: ~30 KB
- Ladezeit: < 100ms
- Empfohlen: Max. 100-200 Releases

**API:**
```
GET  /local/release_data.json
POST /api/release_notes_manager/save
```

## 💬 Support

- [GitHub Repository](https://github.com/atheile-ha/ha-release-notes-addon)
- [Issues](https://github.com/atheile-ha/ha-release-notes-addon/issues)
- [Discussions](https://github.com/atheile-ha/ha-release-notes-addon/discussions)

## Topics

[home-assistant](https://github.com/topics/home-assistant) · [hacs](https://github.com/topics/hacs) · [custom-integration](https://github.com/topics/custom-integration) · [release-notes](https://github.com/topics/release-notes)
