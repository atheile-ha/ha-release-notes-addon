# Changelog - Release Notes Manager

## [0.6.1] - 2026-08-13

### 🐛 Bugfix

**Update-Tracker: Falsche "Update"-Einträge beim ersten Lauf nach Integrationen ohne sofortigen Datenabruf**
- Bei manchen Integrationen ist `installed_version` beim `EVENT_HOMEASSISTANT_STARTED`-Zeitpunkt noch nicht bekannt (`None`), weil der erste Datenabruf noch aussteht. Die Baseline übernahm diesen `None`-Wert; sobald die Integration kurz darauf ihren echten Wert meldete, wurde das fälschlich als abgeschlossenes Update (`"? → ..."`) dokumentiert
- Ein Wechsel von "noch unbekannt" auf den ersten echten Wert erzeugt jetzt keinen Eintrag mehr, sondern trägt den Cache nur still nach - wie bei der eigentlichen Baseline

### 🔧 Technisch

- Backend-Version: v0.6.1 (`update_tracker.py`)
- Admin-Version: v0.6.0 (unverändert)
- Widget-Version: v0.5.3 (unverändert)

---

## [0.6.0] - 2026-08-13

### 🎉 Neue Features

**Automatische Update-Dokumentation über Home-Assistant-Update-Entitäten**
- Beobachtet alle `update.*`-Entitäten der Instanz und legt bei abgeschlossenen Updates automatisch einen Eintrag `"[alte Version] → [neue Version]"` in der Kategorie "Update" an
- Neu hinzukommende bzw. verschwindende Update-Entitäten (Integration/Add-on installiert bzw. deinstalliert) werden ebenfalls dokumentiert (Kategorie "Integration / Addon")
- Erkennung basiert auf einem persistierten Versions-Cache statt auf der reinen on/off-Transition, damit Updates, die einen HA-Neustart erfordern, zuverlässig erkannt werden
- Sammelt mehrere Ereignisse (5 Minuten bei laufendem Betrieb, 2 Minuten ab HA-Start bei Neustart-Updates) zu einer gemeinsamen Benachrichtigung
- Erstlauf nach Aktivierung legt nur eine stille Baseline an, ohne Alt-Einträge für längst installierte Komponenten zu erzeugen
- Neuer Einstellungsbereich im Admin-Dashboard (⚙️ Einstellungen) zum Ein-/Ausschalten der Funktion (Standard: aktiviert)
- Versionierung neu erstellter Tages-Releases folgt einem fortlaufenden Zähler pro Monat (`YYYY.M.N`)

### 🔧 Technisch

- Neues Modul `update_tracker.py`
- Admin-Version: v0.6.0 (Settings-Toggle)
- Backend-Version: v0.6.0 (Update-Tracker, Storage-Settings-Default)
- Widget-Version: v0.5.3 (unverändert)

---

## [0.5.5] - 2026-08-13

### 🎉 Neue Features

**Admin: Einträge innerhalb eines Bereichs per Drag'n'Drop umsortieren**
- Ein Eintrag lässt sich jetzt auch direkt auf einem anderen Eintrag im selben Bereich ablegen, um ihn davor oder danach einzusortieren (statt nur zwischen "Neue Features" und "Änderungen/Bugfixes" zu wechseln)
- Ob vor oder nach dem Zieleintrag eingefügt wird, richtet sich danach, ob in der oberen oder unteren Hälfte der Zielkarte losgelassen wird; eine blaue Linie zeigt die Einfügeposition während des Ziehens an
- Funktioniert auch bereichsübergreifend: Ablegen auf einer konkreten Karte im jeweils anderen Bereich positioniert den Eintrag dort gezielt, statt ihn immer nur oben einzufügen

### 🔧 Technisch

- Admin-Version: v0.5.5 (Drag'n'Drop-Umsortierung)
- Backend-Version: v0.5.2 (unverändert)
- Widget-Version: v0.5.3 (unverändert)

---

## [0.5.4] - 2026-08-13

### 🎉 Neue Features

**Admin: Drag'n'Drop zwischen "Neue Features" und "Änderungen/Bugfixes"**
- Einträge im Release-Bearbeiten-Formular lassen sich per Ziehpunkt (⠿) zwischen den beiden Abschnitten verschieben, ohne sie löschen und neu anlegen zu müssen
- Ziel-Abschnitt wird während des Ziehens optisch hervorgehoben

### 🔧 Technisch

- Admin-Version: v0.5.4 (Drag'n'Drop)
- Backend-Version: v0.5.2 (unverändert)
- Widget-Version: v0.5.3 (unverändert)

---

## [0.5.3] - 2026-08-12

### 🎉 Neue Features

**Admin: Einstellungen-Popup mit Export / Import**
- Neue Schaltfläche "🔧 Einstellungen" im Admin-Interface zwischen "Kategorien" und "+ Neues Release" öffnet ein Popup mit Abschnitt "💾 Daten"
- Export lädt den aktuellen Datenstand (Releases, bekannte Fehler, Kategorien) als JSON-Datei herunter
- Import liest eine JSON-Datei ein und ersetzt nach Bestätigung den aktuellen Datenstand vollständig damit
- Nur im Admin-Interface verfügbar, nicht im Widget
- Das Einstellungen-Popup ist bewusst erweiterbar angelegt, um künftig weitere Einstellungen (z.B. Darstellung, Zugriff) als eigene Abschnitte aufzunehmen

### 🐛 Bugfixes

**Versions-Tracking von Backend/Admin/Widget entkoppelt**
- Der `/api/release_notes_manager/version`-Endpoint lieferte bisher nur eine einzelne Versionsnummer, gegen die sowohl das Admin- als auch das Widget-Dashboard verglichen wurden - obwohl beide unabhängig voneinander versioniert werden. Dadurch stimmten Widget- und Backend-Version strukturell nie überein, was bei jedem neuen Browser/Gerät einen unnötigen Reload des kompletten Dashboards auslöste (`window.parent.location.reload()`).
- Der Endpoint liefert jetzt `{"backend": ..., "admin": ..., "widget": ...}`; jedes Dashboard vergleicht nur noch seine eigene Version.
- Titel, Meta-Tag und Versions-Fußzeile beider Dashboards werden jetzt aus je einer einzigen JS-Konstante abgeleitet statt an mehreren Stellen einzeln hartcodiert zu sein (u.a. stand im Admin-Meta-Tag noch "0.5.0", im Widget-Titel noch "v0.3.0").

**Admin: Zeilenumbrüche in Bearbeitungsfeldern**
- Beim erneuten Öffnen eines Releases zum Bearbeiten wurden mehrzeilige Detailtexte mit literalem `<br>` statt echten Zeilenumbrüchen angezeigt. Ursache: Die `esc()`-Funktion für die Leseansicht wandelt `\n` in `<br>` um und wurde fälschlich auch zum Befüllen der Eingabefelder verwendet. Neue Funktion `escInput()` (ohne `<br>`-Umwandlung) wird jetzt für alle `value`-Attribute und `<textarea>`-Inhalte verwendet.

### 🔧 Technisch

- Backend-Version: v0.5.2 (Versions-API umgebaut)
- Admin-Version: v0.5.3 (Versions-Check-Fix, Zeilenumbruch-Fix, Export/Import)
- Widget-Version: v0.5.3 (Versions-Check-Fix)
- `hacs.json`: Mindest-HA-Version auf 2024.7.0 korrigiert (vorher 2023.1.0 - `StaticPathConfig`/`async_register_static_paths`, seit v0.5.0 verwendet, gibt es erst ab HA 2024.7)
- `storage.py`: totes Cache-Überbleibsel aus `async_save()` entfernt
- `INFO.md` entfernt: war durch einen Merge-Unfall in der v0.5.1-Historie verloren gegangen (README verlinkte seitdem ins Leere) und duplizierte ohnehin größtenteils die README. Inhalte (Verwendung, Troubleshooting) in README.md übernommen; `hacs.json` bekommt stattdessen `"render_readme": true`, damit HACS die README statt des (seit HACS 2.0 kaum noch genutzten) info.md anzeigt

---

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
