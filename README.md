# Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/atheile-ha/ha-release-notes-manager.svg)](https://github.com/atheile-ha/ha-release-notes-manager/releases)
[![License](https://img.shields.io/github/license/atheile-ha/ha-release-notes-manager.svg)](LICENSE)

Ein umfassendes Release Notes Management System für Home Assistant mit Admin-Interface und Widget-Support.

**Version:** v0.4.1 (Frontend) / v0.3.1 (Backend) / v0.1.2 (Widget)

## 🌟 Features

### Admin-Version (release-notes.html)

- ✅ **Release-Verwaltung** - Erstellen, Bearbeiten, Löschen von Releases
- ✅ **Kategorien-System** - 11 Farben, individuell anpassbar
- ✅ **Features, Änderungen, Bekannte Fehler** - Strukturierte Erfassung
- ✅ **Details ein-/ausklappbar** - Übersichtliche Darstellung
- ✅ **Summary Badges** - Schneller Überblick im Header (Features/Änderungen/Fehler)
- ✅ **Pagination** - Initial 10 Releases, "Weitere laden" Button
- ✅ **Suchfunktion** - Durchsucht alle Releases
- ✅ **Filter** - Nach Kategorien filtern
- ✅ **Neuestes Release hervorgehoben** - Blauer Header
- ✅ **LocalStorage** - Persistente Speicherung
- ✅ **Cache-Busting** - Automatische Updates

### Widget-Version (release-notes-widget.html) 🆕

- ✅ **Read-Only** - Nur Anzeige, keine Bearbeitungsmöglichkeit
- ✅ **Auto-Reload** - Erkennt Änderungen automatisch (alle 10s) **NEU in v0.4.1!**
- ✅ **Auto-Collapse** - Konfigurierbar (0, 10-300s)
- ✅ **Smart Display** - Nur neuestes Release initial
- ✅ **"Alle Releases anzeigen"** - Button lädt alle auf einmal
- ✅ **"Nur neuestes Release"** - Zurück zur Einzelansicht
- ✅ **Settings-Panel** - ⚙️ mit Slider für Auto-Collapse
- ✅ **Timer-Logik** - Stoppt bei Interaktion, startet neu bei Collapse
- ✅ **Gleiche Daten** - Nutzt localStorage der Admin-Version

## 📦 Installation

### Via HACS (Empfohlen)

1. HACS öffnen
2. "Integrationen" → ⋮ → "Benutzerdefinierte Repositorys"
3. Repository hinzufügen:
   - URL: `https://github.com/atheile-ha/ha-release-notes-manager`
   - Kategorie: Integration
4. "Release Notes Manager" suchen und installieren
5. Home Assistant neu starten

### Manuell

1. `custom_components/release_notes_manager/` Ordner in `/config/custom_components/` kopieren
2. Home Assistant neu starten
3. HTML-Dateien werden automatisch nach `/config/www/release-notes/` kopiert

## 🚀 Verwendung

### Admin-Version

**URL:**
```
http://DEINE-IP:8123/local/release-notes/release-notes.html
```

**Funktionen:**
1. **Neues Release:** Klick auf "+ Neues Release"
2. **Kategorien:** Klick auf "⚙️" im Header
3. **Bearbeiten:** Klick auf "✏️" beim Release
4. **Details:** Klick auf "▶ Details anzeigen"

### Widget-Version

**URL:**
```
http://DEINE-IP:8123/local/release-notes/release-notes-widget.html
```

**Dashboard-Integration:**

```yaml
type: iframe
url: /local/release-notes/release-notes-widget.html
aspect_ratio: 100%
```

**Funktionen:**
1. **Alle laden:** Klick auf "Alle Releases anzeigen"
2. **Zurück:** Klick auf "Nur neuestes Release"
3. **Settings:** Klick auf "⚙️" → Auto-Collapse einstellen (0-300s)
4. **Auto-Reload:** Widget aktualisiert sich automatisch bei Änderungen (alle 10s)

## 📊 Daten-Speicherung

**LocalStorage:**
- `ha_releases` - Release-Daten
- `ha_categories` - Kategorien

**Gemeinsame Daten:**
- Admin-Version: Lesen + Schreiben
- Widget-Version: Nur Lesen + Auto-Reload bei Änderungen
- Änderungen im Admin sind automatisch im Widget sichtbar (max. 10s)

## 🔄 Update

### Via HACS
1. HACS → Integrationen → Release Notes Manager
2. Update auf v0.4.1
3. Home Assistant neu starten
4. **Fertig!** Widget lädt sich automatisch neu

### Von v0.4.0 zu v0.4.1
- ✅ Widget: Auto-Reload Feature (erkennt Änderungen automatisch)
- ✅ Widget: Kein Platzhalter mehr für nicht-sichtbare Releases
- ✅ Daten bleiben erhalten

## 🆕 Changelog v0.4.1

### Widget v0.1.2 (NEU!)

**Auto-Reload Feature:**
- ✅ Widget checkt alle 10 Sekunden localStorage
- ✅ Automatisches Neu-Laden bei Änderungen
- ✅ CPU-Last: 0.00011% (vernachlässigbar)
- ✅ Keine manuelle URL-Änderung mehr nötig
- ✅ Funktioniert auch in Side Panel

**Fixes:**
- ✅ Kein Platzhalter für nicht-sichtbare Releases
- ✅ Kompaktere Darstellung

Siehe [CHANGELOG.md](CHANGELOG.md) für Details.

## 🐛 Bekannte Probleme

Keine bekannten Probleme in v0.4.1.

## 📝 Lizenz

MIT License - siehe [LICENSE](LICENSE)

## 👤 Autor

Entwickelt von atheile-ha für Home Assistant Community

## 🤝 Beitragen

Issues und Pull Requests sind willkommen!

1. Fork das Repository
2. Erstelle einen Feature-Branch
3. Commit deine Änderungen
4. Push zum Branch
5. Erstelle einen Pull Request

## ⭐ Support

Wenn dir dieses Projekt gefällt, gib ihm einen Stern! ⭐

---

**Bei Fragen oder Problemen:**
- [Issue erstellen](https://github.com/atheile-ha/ha-release-notes-manager/issues)
- [Diskussionen](https://github.com/atheile-ha/ha-release-notes-manager/discussions)
