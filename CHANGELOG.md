# Changelog

## [0.5.0] - 2026-01-02

### 🎯 Major Architecture Modernization

Version 0.5.0 modernisiert die Integration nach Home Assistant Best Practices.

**Breaking Changes:**
- URL-Änderung: `/local/release-notes/` → `/release-notes/`
- Dashboard YAML muss aktualisiert werden (siehe Upgrade-Guide)

### ✨ Features

**HA-Storage Migration**
- ✅ Daten jetzt in `/config/.storage/release_notes_manager`
- ✅ Nutzt offizielle `homeassistant.helpers.storage.Store` API
- ✅ Automatische Backups durch HA-Infrastruktur
- ✅ Atomic writes (kein Datenverlust bei Crash)

**Frontend-Serving Modernisiert**
- ✅ HTML-Dateien direkt aus Integration ausgeliefert
- ✅ Keine Kopien mehr nach `/config/www/`
- ✅ Nutzt `StaticPathConfig` (HA Best Practice)
- ✅ Kein Cache-Problem bei Updates
- ✅ Update-sicher via HACS

**Automatische Migration**
- ✅ Bestehende Daten werden beim ersten Start automatisch migriert
- ✅ Alte Datei wird als `.migrated` gesichert (Rollback möglich)
- ✅ Migration läuft exakt einmal
- ✅ Kein manueller Eingriff nötig
- ✅ Bei Fehler: Alte Daten bleiben erhalten

### 🔧 Changed

**storage.py**
- Komplett modernisiert mit `Store` API
- Migration-Logik implementiert
- Method-Naming: `async_save()` statt `save_all_data()`
- Bessere Fehlerbehandlung

**__init__.py**
- Entfernt: `deploy_www_files()` (Kopier-Logik)
- Neu: `async_register_static_paths()` (StaticPathConfig)
- Vereinfacht: Kein `storage_type` Parameter mehr
- Logging verbessert

**api.py**
- Method-Namen HA-konform (`async_save`)
- Vereinfacht: `require_token` Parameter entfernt
- API-Endpoint bleibt gleich (kein Breaking Change für HTML)

### 🐛 Fixed

**Cache-Probleme**
- ✅ `cache_headers=False` verhindert Browser-Cache
- ✅ Kein `shutil.copy2` mehr = keine Timestamp-Probleme
- ✅ Updates via HACS funktionieren zuverlässig

**HACS-Installation**
- ✅ Keine www/ Ordner-Konflikte mehr
- ✅ HTML-Dateien bleiben in Integration
- ✅ Kein manuelles Kopieren nötig

**Datensicherheit**
- ✅ Atomic writes via HA-Storage
- ✅ Automatische Backups
- ✅ Keine Datenverluste bei Crashes

### 📚 Documentation

- ✅ UPGRADE_v0.5.0.md - Schritt-für-Schritt Upgrade-Guide
- ✅ TECHNICAL_CHANGES_v0.5.0.md - Technische Details
- ✅ README aktualisiert mit neuen URLs
- ✅ Troubleshooting-Guide erweitert

### ⚠️ Migration Notes

**Automatisch migriert:**
- `/config/www/release_data.json` → `/config/.storage/release_notes_manager`

**Manuell aktualisieren:**
- Dashboard URLs: `/local/release-notes/...` → `/release-notes/...`

**Für Rollback bewahrt:**
- `/config/www/release_data.json.migrated` (alte Daten)

**Siehe:** UPGRADE_v0.5.0.md für Details

---

## [0.4.0] - 2026-01-02

### ✨ Frontend Features (11 neue Features)

**Feature 1-3: Delete & Icons**
- ✅ Delete-Button mit 🗑️ Icon
- ✅ Kategorie-Icons (🎨)
- ✅ Sortierung (Version, Datum, Kategorie)

**Feature 4-6: Color & Badges**
- ✅ Color-Picker für Kategorien (11 Farben)
- ✅ Badge-System (Features/Änderungen/Fehler Count)
- ✅ Neuestes Release hervorgehoben (Blauer Header)

**Feature 7-9: Summary & Header**
- ✅ Summary Badges im Header (Schnellübersicht)
- ✅ Blue Header für neuestes Release
- ✅ Pagination ("Weitere laden" Button)

**Feature 10-11: Details & Version**
- ✅ Details Toggle (▶/▼ statt Text)
- ✅ Version Footer (Backend/Frontend Version)

### 🆕 Widget v0.1.2

**Auto-Reload Feature:**
- ✅ Erkennt Änderungen automatisch (alle 10s)
- ✅ CPU-Last: 0.00011% (vernachlässigbar)
- ✅ Funktioniert in Side Panel
- ✅ Max. Verzögerung: 10 Sekunden

**Layout-Fixes:**
- ✅ Kein Platzhalter für nicht-sichtbare Releases
- ✅ Kompakte Darstellung
- ✅ Expandiert nur bei Bedarf

### 🔧 Backend v0.3.1

**Unverändert:**
- ✅ 100% kompatibel mit v0.3.1
- ✅ REST API funktioniert weiterhin
- ✅ Storage in /config/www/release_data.json
- ✅ Daten bleiben erhalten

### 🐛 Fixes

**Cache-Problem behoben:**
- ✅ __init__.py kopiert HTML IMMER (auch wenn existiert)
- ✅ Meta-Tag Version 0.4.0 für Cache-Busting
- ✅ Updates funktionieren zuverlässig
- ✅ **Empfehlung:** Nutze `?` am URL-Ende (verhindert Browser-Cache)

**Widget-Layout:**
- ✅ min-height aus .release-bottom-row entfernt
- ✅ Kein Leerraum mehr für nicht-sichtbare Releases
- ✅ **Empfehlung:** aspect_ratio: 200% für optimale Darstellung

---

## [0.3.1] - 2024-12-15

### Backend-Version (Basis für v0.4.0 und v0.5.0)

**Features:**
- ✅ REST API mit /api/release_notes_manager/save
- ✅ JSON Storage in /config/www/release_data.json
- ✅ Cache-System (5 Minuten)
- ✅ Backup bei jedem Speichern

---

**Legende:**
- ✨ Neue Features
- 🔧 Verbesserungen  
- 🐛 Bugfixes
- 🆕 Neue Komponenten
- ⚠️ Breaking Changes
