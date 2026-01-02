# Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/atheile-ha/ha-release-notes-manager.svg)](https://github.com/atheile-ha/ha-release-notes-manager/releases)
[![License](https://img.shields.io/github/license/atheile-ha/ha-release-notes-manager.svg)](LICENSE)

Ein umfassendes Release Notes Management System für Home Assistant mit Admin-Interface und Widget-Support.

**Version:** v0.4.0

## 🌟 Features

### Admin-Version (release-notes.html)

- ✅ **Release-Verwaltung** - Erstellen, Bearbeiten, Löschen von Releases
- ✅ **Kategorien-System** - 11 Farben, individuell anpassbar
- ✅ **Features, Änderungen, Bekannte Fehler** - Strukturierte Erfassung
- ✅ **Details ein-/ausklappbar** - Übersichtliche Darstellung (▶/▼)
- ✅ **Summary Badges** - Schneller Überblick im Header (Features/Änderungen/Fehler)
- ✅ **Pagination** - Initial 10 Releases, "Weitere laden" Button
- ✅ **Neuestes Release hervorgehoben** - Blauer Header
- ✅ **Delete-Button** - Mit Icon 🗑️
- ✅ **Backend-Persistenz** - Speicherung in /config/www/release_data.json

### Widget-Version (release-notes-widget.html)

- ✅ **Read-Only** - Nur Anzeige, keine Bearbeitungsmöglichkeit
- ✅ **Auto-Reload** - Erkennt Änderungen automatisch (alle 10s)
- ✅ **Auto-Collapse** - Konfigurierbar (0, 10-300s)
- ✅ **Smart Display** - Nur neuestes Release initial
- ✅ **"Alle Releases anzeigen"** - Button lädt alle auf einmal
- ✅ **"Nur neuestes Release"** - Zurück zur Einzelansicht
- ✅ **Settings-Panel** - ⚙️ mit Slider für Auto-Collapse
- ✅ **Kein Platzhalter** - Expandiert nur bei Bedarf

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
http://DEINE-IP:8123/local/release-notes/release-notes.html?
```

**Tipp:** Das `?` am Ende verhindert Browser-Cache und zeigt immer die neueste Version!

**Funktionen:**
1. **Neues Release:** Klick auf "+ Neues Release"
2. **Kategorien:** Klick auf "⚙️" im Header
3. **Bearbeiten:** Klick auf "✏️" beim Release
4. **Details:** Klick auf "▶ Details anzeigen"
5. **Löschen:** Klick auf 🗑️ Button

### Widget-Version

**URL:**
```
http://DEINE-IP:8123/local/release-notes/release-notes-widget.html?
```

**Tipp:** Das `?` am Ende verhindert Browser-Cache!

**Dashboard-Integration:**

```yaml
type: iframe
url: /local/release-notes/release-notes-widget.html?
aspect_ratio: 200%
```

**Wichtig:**
- `?` am URL-Ende verhindert Browser-Cache (zeigt immer aktuelle Version)
- `aspect_ratio: 200%` passt sich gut an Widget-Höhe an (anpassbar nach Bedarf)

**Funktionen:**
1. **Alle laden:** Klick auf "Alle Releases anzeigen"
2. **Zurück:** Klick auf "Nur neuestes Release"
3. **Settings:** Klick auf "⚙️" → Auto-Collapse einstellen (0-300s)
4. **Auto-Reload:** Widget aktualisiert sich automatisch bei Änderungen (alle 10s)

## 📊 Daten-Speicherung

**Backend:**
- Speicherort: `/config/www/release_data.json`
- API: `/api/release_notes_manager/save`
- Backup: Automatisch bei jedem Speichern

**Cache:**
- Dauer: 5 Minuten
- Auto-Invalidierung bei Änderungen

## 🔄 Update

### Via HACS
1. HACS → Integrationen → Release Notes Manager
2. Update auf v0.4.0
3. Home Assistant neu starten
4. **Fertig!** HTML-Dateien werden automatisch aktualisiert

### Von v0.3.1 zu v0.4.0
- ✅ Backend: Unverändert (100% kompatibel)
- ✅ Frontend: 11 neue Features
- ✅ Widget: Neu hinzugefügt
- ✅ Daten bleiben erhalten

## 🆕 Changelog v0.4.0

### Frontend v0.4.0 (11 Features)

1. ✅ **Delete-Button mit Icon** (🗑️)
2. ✅ **Icons für Kategorien** (🎨)
3. ✅ **Sortierung** (Version, Datum, Kategorie)
4. ✅ **Color-Picker** (11 Farben)
5. ✅ **Badges** (Features/Änderungen/Fehler Count)
6. ✅ **Neuestes Release** (Blauer Header)
7. ✅ **Summary Badges** (Schnellübersicht)
8. ✅ **Blue Header** (Highlight)
9. ✅ **Weitere laden** (Pagination)
10. ✅ **Details Toggle** (▶/▼)
11. ✅ **Version Footer** (Backend/Frontend Version)

### Widget v0.1.2

- ✅ Auto-Reload (10s Intervall, CPU: 0.00011%)
- ✅ Kein Platzhalter für nicht-sichtbare Releases
- ✅ Kompakte Darstellung

### Backend v0.3.1

- ✅ Unverändert (100% kompatibel)
- ✅ REST API funktioniert weiterhin

### Fixes

- ✅ Cache-Problem behoben (HTML wird bei HA-Start aktualisiert)
- ✅ Widget Platzhalter entfernt (min-height fix)

## 🐛 Bekannte Probleme

Keine bekannten Probleme in v0.4.0.

## 📝 Lizenz

MIT License - siehe [LICENSE](LICENSE)

## 👤 Autor

Entwickelt von atheile-ha für Home Assistant Community

## 🤝 Beitragen

Issues und Pull Requests sind willkommen!

---

**Bei Fragen oder Problemen:**
- [Issue erstellen](https://github.com/atheile-ha/ha-release-notes-manager/issues)
