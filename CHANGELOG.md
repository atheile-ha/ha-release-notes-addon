# Changelog - Release Notes Manager

## [0.5.2] - 2026-01-03

### 🐛 Bugfixes

**Widget: Fehlende Fixes nachgeholt**
- Badge-Zählung im Widget korrigiert: Gelöste Known Issues werden jetzt mitgezählt
- Zeilenumbrüche im Widget funktionieren jetzt korrekt

**Hinweis:** Diese Fixes waren in v0.5.1 nur im Admin-Interface, nicht im Widget vorhanden.

### 🔧 Technisch

- Widget-Version: v0.5.2
- Backend-Version: v0.5.1 (unverändert)
- Admin-Version: v0.5.1 (unverändert)

---

## [0.5.1] - 2026-01-02

### 🎉 Neue Features

**Auto-Reload bei Updates**
- Widget und Admin-Interface prüfen automatisch Backend-Version
- Bei Versions-Mismatch: Automatischer Reload (einmalig)
- Kein manuelles Cache-Busting mehr nötig!
- localStorage verhindert Reload-Loops

### 🐛 Bugfixes

**Zeilenumbrüche in Textfeldern**
- Beschreibungen, Changelogs und Known Issues zeigen jetzt Zeilenumbrüche korrekt an
- `esc()` Funktion konvertiert `\n` → `<br>`
- Betrifft: Admin-Interface und Dashboard-Widget

**Gelöste Fehler in Badge-Zählung**
- Gelöste Known Issues werden jetzt im Änderungs-Badge mitgezählt
- Vorher: Nur explizite "Änderungen" gezählt
- Jetzt: Änderungen + gelöste Fehler dieser Version
- Beispiel: 3 Änderungen + 2 gelöste Bugs = Badge "5 Änderungen"

### 🔧 Technisch

- API-Endpoint hinzugefügt: `GET /api/release_notes_manager/version`
- Auto-Reload JavaScript in Widget und Admin
- `esc()` Funktion erweitert: `.replace(/\n/g,'<br>')`
- `getSummaryBadges()` zählt gelöste Issues
- Frontend-Version: v0.5.1
- Backend-Version: v0.5.1

---

## [0.5.0] - 2026-01-02

### 🎯 Major Changes

**HA-Storage Migration**
- Daten werden in `.storage/release_notes_manager` gespeichert
- Automatische Migration von v0.4.0 Daten beim ersten Start
- Rollback-Sicherheit: Alte Daten werden als `.migrated` gesichert

**Frontend-Serving modernisiert**
- Assets direkt aus Integration bereitgestellt
- Kein Kopieren nach `/config/www/` mehr nötig
- Neue URLs: `/release-notes/` statt `/local/release-notes/`

**API modernisiert**
- GET-Endpoint: `/api/release_notes_manager/data` - Daten laden
- POST-Endpoint: `/api/release_notes_manager/data` - Daten speichern
- Nur offizielle Home Assistant APIs verwendet

### ✅ Features erhalten

Alle 11 Features aus v0.4.0 vollständig erhalten:
- Suche und Filterung
- Kategorien und Status
- Known Issues Tracking
- Dark Mode, Responsive Design
- Auto-Reload, Changelog-Ansicht
- Badge-System, Import/Export
- Backup-Funktionen
- Multi-Language (DE)

### 🐛 Bugfixes

**Critical: Cache-Bug behoben**
- Cache verhinderte Migration beim ersten Start
- Symptom: HA-Storage blieb leer (0 releases)
- Fix: Cache-System entfernt (HA-Storage ist schnell genug)
- Migration läuft jetzt garantiert

**HTML-Versionen korrigiert**
- Meta-Tags auf v0.5.0 aktualisiert
- Footer zeigt korrekte Versionen
- Admin: "Backend v0.5.0 | Frontend v0.5.0"
- Widget: "Backend v0.5.0 | Widget v0.5.0"

**API-Endpoint hinzugefügt**
- v0.5.0 (initial) hatte nur POST-Endpoint
- GET-Endpoint fehlte → HTML konnte Daten nicht laden
- Fix: GET + POST in einem Endpoint vereint

### ⚠️ Breaking Changes

**Dashboard-URLs geändert:**
```yaml
# ALT (v0.4.0):
url: /local/release-notes/release-notes-widget.html?

# NEU (v0.5.0):
url: /release-notes/release-notes-widget.html?
```

**Datenspeicherung:**
- ALT: `/config/www/release_data.json`
- NEU: `/config/.storage/release_notes_manager`

**Automatische Migration:**
- Erfolgt beim ersten Start nach Update
- Alte Datei wird als `.migrated` gesichert
- Kein Datenverlust möglich

### 📊 Getestet mit

- Home Assistant 2025.12.5
- Migration von v0.4.0 mit 37+ releases
- HACS Installation
- Manuelle Installation

---

## [0.4.0] - 2025-12-XX

### Features
- 11 neue Features
- UI-Verbesserungen
- Performance-Optimierungen
- Vollständiges Admin-Interface
- Dashboard-Widget

---

## [0.3.x] - 2025-11-XX

### Initial Release
- Erste HACS-Version
- Basis-Release-Verwaltung
- Einfaches Frontend

---

**Repository:** https://github.com/atheile-ha/ha-release-notes-manager  
**HACS:** Custom Repository  
**Lizenz:** MIT
