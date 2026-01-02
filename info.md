# Release Notes Manager für Home Assistant

Ein elegantes Tool zur Verwaltung und Anzeige von Release Notes direkt in Home Assistant.

## ✨ Hauptfunktionen

### 📋 Release-Verwaltung
- **Versionsmanagement:** Übersichtliche Verwaltung aller Releases mit Versionsnummern
- **Kategorisierung:** Releases nach Kategorien strukturieren (Features, Bugfixes, Breaking Changes, etc.)
- **Known Issues:** Bekannte Probleme direkt zu Releases zuordnen und verfolgen
- **Status-Tracking:** Releases als "veröffentlicht", "geplant" oder "in Entwicklung" markieren

### 🎨 Benutzeroberfläche
- **Admin-Interface:** Vollständiges Verwaltungs-Interface zum Erstellen und Bearbeiten von Releases
- **Dashboard-Widget:** Kompaktes Widget zur Anzeige der neuesten Releases im Dashboard
- **Dark Mode:** Automatische Anpassung an das Home Assistant Theme
- **Responsive Design:** Optimiert für Desktop, Tablet und Mobile

### 🔍 Erweiterte Features
- **Suche:** Releases nach Versionsnummern, Titeln oder Inhalten durchsuchen
- **Filterung:** Nach Kategorien und Status filtern
- **Changelog-Ansicht:** Detaillierte Änderungsprotokolle für jedes Release
- **Auto-Reload:** Widget aktualisiert sich automatisch bei Änderungen

## 🆕 Version 0.5.0 - HA-Storage Migration

### Hauptänderungen

#### ✅ HA-Storage basiert
- **Moderne Datenhaltung:** Daten werden in Home Assistant's offiziellem Storage-System gespeichert
- **Automatische Migration:** v0.4.0 Daten werden beim ersten Start automatisch migriert
- **Rollback-Sicherheit:** Alte Daten werden als `.migrated` gesichert

#### ✅ Frontend-Serving modernisiert
- **Direkte Integration:** Assets werden direkt aus der Integration bereitgestellt
- **Keine Datei-Duplikate:** Kein Kopieren nach `/config/www/` mehr nötig
- **Saubere URLs:** Neue URLs unter `/release-notes/`

#### ✅ API modernisiert
- **GET-Endpoint:** Daten können geladen werden (`GET /api/release_notes_manager/data`)
- **POST-Endpoint:** Daten speichern (`POST /api/release_notes_manager/data`)
- **HA-konform:** Nutzt nur offizielle Home Assistant APIs

### Alle v0.4.0 Features erhalten

✅ **Keine Features entfernt!** Alle 11 Features aus v0.4.0 sind vollständig erhalten:
- Suche und Filterung
- Kategorien und Status
- Known Issues Tracking
- Dark Mode
- Responsive Design
- Auto-Reload
- Changelog-Ansicht
- Badge-System
- Import/Export
- Backup-Funktionen
- Multi-Language Support (DE)

## 🚀 Installation

### Via HACS (empfohlen)

1. HACS öffnen
2. "Integrationen" → Menü (⋮) → "Benutzerdefinierte Repositories"
3. Repository hinzufügen: `https://github.com/DEIN-USERNAME/ha-release-notes-manager`
4. Kategorie: "Integration"
5. "Release Notes Manager" suchen und installieren
6. Home Assistant neu starten

### Manuelle Installation

1. Kopiere den `custom_components/release_notes_manager` Ordner nach `/config/custom_components/`
2. Home Assistant neu starten

## ⚙️ Konfiguration

### configuration.yaml

```yaml
# Release Notes Manager aktivieren
release_notes_manager:

# Optional: Debug-Logging
logger:
  default: info
  logs:
    custom_components.release_notes_manager: debug
```

### Dashboard-Integration

**Admin-Interface als Dashboard-Tab:**
```yaml
title: Release Notes
icon: mdi:note-text
url: /release-notes/release-notes.html?
```

**Widget für Übersichts-Dashboard:**
```yaml
type: iframe
url: /release-notes/release-notes-widget.html?
aspect_ratio: 200%
```

## 📊 Screenshots

### Admin-Interface
Vollständiges Verwaltungs-Interface mit allen Features:
- Release erstellen/bearbeiten/löschen
- Kategorien verwalten
- Known Issues zuordnen
- Suche und Filterung
- Status-Management

### Dashboard-Widget
Kompakte Ansicht der neuesten Releases:
- Neueste 5 Releases
- Quick-Actions
- Auto-Reload
- Link zum Admin-Interface

## 🔄 Upgrade von v0.4.0

### Automatische Migration

Die Migration erfolgt **vollautomatisch** beim ersten Start nach dem Update:

1. **Update installieren** (via HACS oder manuell)
2. **HA neu starten**
3. **Migration läuft automatisch:**
   - Alte Daten aus `/config/www/release_data.json` werden gelesen
   - In HA-Storage migriert
   - Alte Datei wird als `.migrated` gesichert
4. **Dashboard URLs aktualisieren** (siehe Breaking Changes)

### ⚠️ Breaking Changes

**Dashboard-URLs haben sich geändert:**

```yaml
# ALT (v0.4.0):
url: /local/release-notes/release-notes-widget.html?

# NEU (v0.5.0):
url: /release-notes/release-notes-widget.html?
```

**Nach dem Update:**
1. Dashboard im Bearbeitungsmodus öffnen
2. iframe-Card mit dem Widget öffnen
3. URL anpassen: `/local/release-notes/` → `/release-notes/`
4. Speichern
5. Browser-Cache leeren (Strg+Shift+R)

### Rollback (falls nötig)

Falls Probleme auftreten:

```bash
# 1. Alte Datei wiederherstellen
cp /config/www/release_data.json.migrated \
   /config/www/release_data.json

# 2. v0.4.0 über HACS neu installieren
# 3. HA neu starten
# 4. URLs in Dashboard zurück auf /local/release-notes/
```

**Kein Datenverlust möglich** - alle Daten bleiben erhalten!

## 📁 Datenspeicherung

### v0.5.0 (HA-Storage)

**Primär:**
```
/config/.storage/release_notes_manager
```
- Offizielle HA-Storage Methode
- Automatische Backups durch HA
- Atomic Writes (keine Korruption)
- Versionierung

**Backup (nach Migration):**
```
/config/www/release_data.json.migrated
```
- Für Rollback zu v0.4.0
- Kann nach erfolgreichem Test gelöscht werden

### Alte Dateien aufräumen (optional)

Nach erfolgreichem Update und Test:

```bash
# Alte Backups löschen (optional)
rm /config/www/release_data.json.backup
rm /config/www/release_data.json.BACKUP_BEFORE_v0.5.0

# Alte HTML-Kopien löschen (optional)
rm -rf /config/www/release-notes/
```

**Wichtig:** `.migrated` Datei behalten für möglichen Rollback!


## 📖 Verwendung

### Release erstellen

1. Admin-Interface öffnen (`/release-notes/release-notes.html`)
2. **"+ Neues Release"** klicken
3. Formular ausfüllen:
   - Version (z.B. "2025.1.0")
   - Titel
   - Datum
   - Status (Veröffentlicht/Geplant/In Entwicklung)
   - Kategorie
   - Beschreibung & Changelog
4. **"Speichern"** klicken

### Known Issue hinzufügen

1. Release öffnen (✏️)
2. Zu **"Known Issues"** scrollen
3. **"+ Issue hinzufügen"** klicken
4. Beschreibung eingeben
5. Optional: Lösung/Workaround
6. **"Speichern"**

### Kategorien verwalten

1. Oben rechts **"Kategorien"** klicken
2. Neue Kategorie hinzufügen oder bestehende bearbeiten
3. Farbe und Icon anpassen
4. **"Speichern"**

## 🐛 Troubleshooting

### Releases werden nicht angezeigt

**Lösung 1: Browser-Cache leeren**
```
Strg + Shift + R (Hard Reload)
```

**Lösung 2: Migration prüfen**
```bash
# Prüfe HA-Storage
cat /config/.storage/release_notes_manager | jq '.data.releases | length'

# Falls 0: Migration neu durchführen
cp /config/www/release_data.json.migrated /config/www/release_data.json
rm /config/.storage/release_notes_manager
# HA neu starten
```

**Lösung 3: Logs prüfen**
```
Einstellungen → System → Protokolle
Suche: "release_notes_manager"
```

### 404 Error beim Öffnen

**URL prüfen:**
- ✅ Richtig: `/release-notes/release-notes.html?`
- ❌ Falsch: `/local/release-notes/...` (v0.4.0 URL)

**configuration.yaml prüfen:**
```yaml
release_notes_manager:  # Muss vorhanden sein!
```

### Speichern funktioniert nicht

**Logs prüfen:**
```
Einstellungen → System → Protokolle
Suche: "Error"
```

**API-Endpoint testen:**
```bash
# In Browser Developer Tools (F12) Console:
fetch('/api/release_notes_manager/data')
  .then(r => r.json())
  .then(d => console.log(d))
```

## 📝 Changelog

### v0.5.0 (2026-01-02)

**Major Changes:**
- ✅ Migration zu HA-Storage
- ✅ Frontend-Serving modernisiert
- ✅ API mit GET+POST Endpoints
- ✅ Automatische Migration von v0.4.0
- ✅ Cache-Bug behoben

**Behoben:**
- Cache verhinderte Migration (#BUG-001)
- HTML Versionen nicht aktualisiert (#BUG-002)
- API-Endpoint fehlte für Laden (#BUG-003)

**Breaking Changes:**
- Dashboard URLs: `/local/release-notes/` → `/release-notes/`

### v0.4.0 (2025-12-XX)

- 11 neue Features
- UI-Verbesserungen
- Performance-Optimierungen

### v0.3.x (2025-11-XX)

- Initiale HACS-Version
- Basis-Funktionalität

## 🤝 Support

- **GitHub Issues:** [Repository Issues](https://github.com/DEIN-USERNAME/ha-release-notes-manager/issues)
- **Dokumentation:** [UPGRADE_v0.5.0.md](UPGRADE_v0.5.0.md)
- **Technische Details:** [TECHNICAL_CHANGES_v0.5.0.md](TECHNICAL_CHANGES_v0.5.0.md)

## 📜 Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei

## 👏 Credits

Entwickelt für die Home Assistant Community 🏠

---

**Version:** 0.5.0  
**Letztes Update:** 2026-01-02 
