# Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/atheile-ha/ha-release-notes-manager.svg)](https://github.com/atheile-ha/ha-release-notes-manager/releases)
[![License](https://img.shields.io/github/license/atheile-ha/ha-release-notes-manager.svg)](LICENSE)

Ein umfassendes Release Notes Management System für Home Assistant mit Admin-Interface und Widget-Support.

**Version:** v0.5.0

## 🆕 Neu in v0.5.0 - Architecture Modernization

v0.5.0 modernisiert die Integration nach **Home Assistant Best Practices**:

✅ **HA-Storage** statt `/config/www/` - Offizielle Storage-API  
✅ **Frontend direkt aus Integration** - Keine Kopien mehr  
✅ **Automatische Migration** - Kein Datenverlust beim Update  
✅ **Update-sicher** - HACS überschreibt einfach  
✅ **Keine Cache-Probleme** - Immer aktuelle Version  

**⚠️ Breaking Change:** URLs haben sich geändert!  
`/local/release-notes/...` → `/release-notes/...`

**📖 Upgrade-Guide:** Siehe [UPGRADE_v0.5.0.md](UPGRADE_v0.5.0.md)

---

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
- ✅ **HA-Storage** - Automatische Backups, Atomic Writes

### Widget-Version (release-notes-widget.html)

- ✅ **Read-Only** - Nur Anzeige, keine Bearbeitungsmöglichkeit
- ✅ **Auto-Reload** - Erkennt Änderungen automatisch (alle 10s)
- ✅ **Auto-Collapse** - Konfigurierbar (0, 10-300s)
- ✅ **Smart Display** - Nur neuestes Release initial
- ✅ **"Alle Releases anzeigen"** - Button lädt alle auf einmal
- ✅ **"Nur neuestes Release"** - Zurück zur Einzelansicht
- ✅ **Settings-Panel** - ⚙️ mit Slider für Auto-Collapse
- ✅ **Kein Platzhalter** - Expandiert nur bei Bedarf

---

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
3. Frontend wird automatisch registriert

---

## 🚀 Verwendung

### Admin-Version

**URL:**
```
http://DEINE-IP:8123/release-notes/release-notes.html?
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
http://DEINE-IP:8123/release-notes/release-notes-widget.html?
```

**Tipp:** Das `?` am Ende verhindert Browser-Cache!

**Dashboard-Integration:**

```yaml
type: iframe
url: /release-notes/release-notes-widget.html?
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

---

## 📊 Daten-Speicherung

**v0.5.0 (HA-Storage):**
- Speicherort: `/config/.storage/release_notes_manager`
- API: Offizielle `homeassistant.helpers.storage.Store`
- Backup: Automatisch durch HA-Infrastruktur
- Atomic Writes: Kein Datenverlust bei Crash

**Migration von v0.4.0:**
- Alte Datei: `/config/www/release_data.json`
- Wird automatisch migriert beim ersten Start
- Gesichert als: `/config/www/release_data.json.migrated`
- Rollback möglich (siehe Upgrade-Guide)

---

## 🔄 Update

### Von v0.4.0 zu v0.5.0

**⚠️ WICHTIG:** URLs haben sich geändert!

**Schritt 1:** Update via HACS
```
HACS → Integrationen → Release Notes Manager → Update auf v0.5.0
```

**Schritt 2:** HA neu starten
```
Einstellungen → System → Neustart
```

**Schritt 3:** Dashboard YAML aktualisieren
```yaml
# ALT (v0.4.0)
url: /local/release-notes/release-notes-widget.html?

# NEU (v0.5.0)
url: /release-notes/release-notes-widget.html?
```

**Schritt 4:** Logs prüfen
```
Einstellungen → System → Protokolle
Suche: "release_notes_manager"

Sollte zeigen:
✅ "Starting migration from www/release_data.json"
✅ "Data migrated to HA-Storage successfully"
✅ "Old file preserved as release_data.json.migrated"
```

**Fertig!** Daten wurden automatisch migriert ✅

**Detaillierte Anleitung:** [UPGRADE_v0.5.0.md](UPGRADE_v0.5.0.md)

---

## 🆕 Changelog v0.5.0

### ✨ Major Changes

**HA-Storage Migration**
- ✅ Daten in `/config/.storage/` (HA-Standard)
- ✅ Automatische Backups
- ✅ Atomic Writes

**Frontend Modernisiert**
- ✅ Direkt aus Integration ausgeliefert
- ✅ Keine Kopien nach `/config/www/`
- ✅ Update-sicher via HACS

**Automatische Migration**
- ✅ Beim ersten Start
- ✅ Alte Datei gesichert
- ✅ Kein Datenverlust

### 🔧 Breaking Changes

- URL-Änderung: `/local/release-notes/` → `/release-notes/`
- Dashboard YAML muss aktualisiert werden

**Vollständiges Changelog:** [CHANGELOG.md](CHANGELOG.md)

---

## 🐛 Bekannte Probleme

Keine bekannten Probleme in v0.5.0.

Bei Upgrade-Problemen: Siehe [UPGRADE_v0.5.0.md](UPGRADE_v0.5.0.md#-troubleshooting)

---

## 📝 Lizenz

MIT License - siehe [LICENSE](LICENSE)

---

## 👤 Autor

Entwickelt von atheile-ha für Home Assistant Community

---

## 🤝 Beitragen

Issues und Pull Requests sind willkommen!

---

## 🆘 Support

**Bei Fragen oder Problemen:**
- [Issue erstellen](https://github.com/atheile-ha/ha-release-notes-manager/issues)
- Logs und Fehlermeldungen anhängen
- Version angeben (v0.5.0)

**Dokumentation:**
- [Upgrade Guide](UPGRADE_v0.5.0.md) - Schritt-für-Schritt Anleitung
- [Technical Changes](TECHNICAL_CHANGES_v0.5.0.md) - Entwickler-Details
- [Best Practices](BEST_PRACTICES.md) - Tipps & Tricks (v0.4.0)

---

**Home Assistant konform seit v0.5.0!** ✅
