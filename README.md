# Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/release/atheile-ha/ha-release-notes-addon.svg)](https://github.com/atheile-ha/ha-release-notes-addon/releases)

Web-Anwendung zur Verwaltung von Release Notes direkt in Home Assistant.

## ✨ Features (v0.4.0)

### Release-Verwaltung
- Releases erstellen, bearbeiten und löschen
- Versionierung mit Release-Nummern
- Optionaler Release-Name
- Deutsches Datumsformat
- **Release Summary** - Kompakte Übersicht (Features • Bugs • Status)
- **Markdown Export** - Exportiere Releases als .md Datei

### Kategorisierung
- Neue Features dokumentieren
- Änderungen / Bugfixes festhalten
- Bekannte Fehler tracken
- 6 vordefinierte Kategorien
- Eigene Kategorien erstellen
- **Alphabetische Sortierung** der Kategorien

### Bedienung
- **Keyboard Shortcuts** - Strg+S (Speichern), ESC (Schließen)
- **Dark Mode** - Automatische Anpassung an System-Theme
- **Neue Einträge oben** - Features/Bugs erscheinen am Anfang
- **Pencil Icon** - Kompakter ✏️ Bearbeiten-Button
- **Loading Indicator** - Visuelles Feedback beim Speichern
- Suchfunktion über alle Releases
- Filter nach Kategorien
- Responsive Design
- 100% offline

### Fehler-Management
- Automatische Übernahme offener Fehler
- Fehler als gelöst markieren
- Historie bleibt sichtbar
- Gelöste Fehler wieder öffnen

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

Exportiere einzelne Releases als Markdown-Datei:
- Button "📄 Export MD" bei jedem Release
- Ideal für GitHub Releases
- Perfekt für Dokumentation

## 🌙 Dark Mode

Automatische Unterstützung für Dark Mode basierend auf System-Einstellung. Alle Texte sind optimal lesbar.

## 🆕 Neue Einträge oben

Neu hinzugefügte Features, Änderungen und Bugs erscheinen automatisch am Anfang der jeweiligen Liste - nicht am Ende wie früher.

## 🔍 Troubleshooting

### Integration lädt nicht
1. Prüfe `configuration.yaml`
2. Prüfe Logs: Einstellungen → System → Protokolle
3. Suche nach `release_notes_manager`

### Seite zeigt 404
1. Prüfe Datei: `/config/custom_components/release_notes_manager/www/release-notes.html`
2. Home Assistant neu starten
3. Browser-Cache leeren (Strg+Shift+R)

### Dark Mode unleserlich
- Stelle sicher dass v0.4.0 installiert ist
- Browser Hard Reload: Strg+Shift+R
- Prüfe Version im Tab-Titel (sollte "v0.4.0" zeigen)

### Features nicht sichtbar
1. Prüfe Version: `cat /config/custom_components/release_notes_manager/manifest.json | grep version`
2. Sollte zeigen: `"version": "0.4.0"`
3. Force-Copy: `cp /config/custom_components/release_notes_manager/www/release-notes.html /config/www/release-notes/`
4. Browser: Strg+Shift+R

## 📊 Technische Details

**Anforderungen:**
- Home Assistant 2024.1.0+
- Browser: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

**Performance:**
- Dateigröße: ~33 KB (HTML)
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

## 📝 Changelog

Siehe [CHANGELOG.md](CHANGELOG.md) für Details zu allen Versionen.
