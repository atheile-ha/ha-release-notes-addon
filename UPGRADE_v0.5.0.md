# Upgrade Guide: v0.4.0 → v0.5.0

## 🎯 Was ist neu in v0.5.0?

Version 0.5.0 modernisiert die Architektur nach Home Assistant Best Practices:

### ✨ Hauptänderungen

1. **HA-Storage statt /config/www/**
   - Daten jetzt in `/config/.storage/release_notes_manager`
   - Nutzt offizielle Home Assistant Storage-API
   - Automatische Backups durch HA
   
2. **Frontend direkt aus Integration**
   - Keine Dateien mehr nach `/config/www/release-notes/` kopiert
   - Assets werden direkt aus Integration ausgeliefert
   - Einfachere Updates via HACS

3. **Automatische Migration**
   - Bestehende Daten werden beim ersten Start migriert
   - Alte Datei wird als `.migrated` gesichert
   - Kein manueller Eingriff nötig

---

## 📦 Upgrade-Schritte

### Für HACS-Nutzer

```bash
1. HACS → Integrationen → Release Notes Manager → Update auf v0.5.0
2. Home Assistant neu starten
3. Logs prüfen (siehe unten)
4. Fertig! ✅
```

### Für manuelle Installation

```bash
1. Download v0.5.0.zip von GitHub
2. Entpacken nach /config/custom_components/release_notes_manager/
3. Home Assistant neu starten
4. Logs prüfen (siehe unten)
5. Fertig! ✅
```

---

## 🔍 Nach dem Upgrade prüfen

### 1. Logs kontrollieren

**Einstellungen → System → Protokolle**, suche nach:

```
✅ Setting up Release Notes Manager v0.5.0
✅ Starting migration from www/release_data.json to HA-Storage
✅ Data migrated to HA-Storage successfully: X releases, Y issues
✅ Old file preserved as release_data.json.migrated
✅ Frontend assets registered: /release-notes/
✅ Registered API view: /api/release_notes_manager/save
✅ Release Notes Manager v0.5.0 setup complete
```

### 2. URLs aktualisieren

**WICHTIG:** URLs haben sich geändert!

#### Alte URLs (v0.4.0):
```
/local/release-notes/release-notes.html
/local/release-notes/release-notes-widget.html
```

#### Neue URLs (v0.5.0):
```
/release-notes/release-notes.html
/release-notes/release-notes-widget.html
```

**Dashboard YAML aktualisieren:**

```yaml
# VORHER (v0.4.0)
type: iframe
url: /local/release-notes/release-notes-widget.html?
aspect_ratio: 200%

# NACHHER (v0.5.0)
type: iframe
url: /release-notes/release-notes-widget.html?
aspect_ratio: 200%
```

### 3. Daten-Migration verifizieren

**Methode 1: Via Admin-Interface**
- Öffne: `/release-notes/release-notes.html`
- Prüfe ob alle Releases angezeigt werden
- Teste Speichern

**Methode 2: Via HA-Storage**
```bash
# Prüfe ob neue Storage-Datei existiert:
ls -la /config/.storage/release_notes_manager

# Prüfe ob alte Datei gesichert wurde:
ls -la /config/www/release_data.json.migrated
```

---

## 🗂️ Datei-Struktur nach Upgrade

### ✅ Neue Dateien (v0.5.0)

```
/config/
├── .storage/
│   └── release_notes_manager        ← Neue Datenbank (HA-Storage)
│
└── custom_components/
    └── release_notes_manager/
        ├── __init__.py               ← Modernisiert
        ├── api.py                    ← Angepasst
        ├── storage.py                ← Komplett neu (HA-Storage + Migration)
        ├── manifest.json             ← v0.5.0
        ├── release-notes.html        ← Bleibt in Integration
        └── release-notes-widget.html ← Bleibt in Integration
```

### 🗑️ Alte Dateien (können gelöscht werden)

```
/config/
└── www/
    ├── release_data.json.migrated    ← Gesichert (kann nach Test gelöscht werden)
    ├── release_data.json.backup      ← Alt (kann gelöscht werden)
    └── release-notes/                ← Ganzer Ordner kann gelöscht werden
        ├── release-notes.html        ← Nicht mehr benutzt
        └── release-notes-widget.html ← Nicht mehr benutzt
```

**Nach erfolgreichem Test:**
```bash
# Optional: Alte Dateien entfernen (nach 1 Woche Testphase)
rm -rf /config/www/release-notes/
rm /config/www/release_data.json.backup
# release_data.json.migrated BEHALTEN für Rollback!
```

---

## ↩️ Rollback zu v0.4.0 (falls nötig)

Falls Probleme auftreten:

### Schritt 1: Migration rückgängig machen

```bash
# Alte Datei wiederherstellen
mv /config/www/release_data.json.migrated /config/www/release_data.json
```

### Schritt 2: Downgrade via HACS

```bash
1. HACS → Integrationen → Release Notes Manager
2. Reinstall → v0.4.0 auswählen
3. Home Assistant neu starten
```

### Schritt 3: Dashboard URLs zurücksetzen

```yaml
# Zurück zu alten URLs
type: iframe
url: /local/release-notes/release-notes-widget.html?
aspect_ratio: 200%
```

---

## 🔧 Troubleshooting

### Problem: "Migration failed"

**Ursache:** Alte Datei konnte nicht gelesen werden

**Lösung:**
```bash
# Prüfe ob Datei existiert und lesbar ist:
ls -la /config/www/release_data.json

# Prüfe Dateiinhalt:
cat /config/www/release_data.json | head -20

# Falls korrupt: Aus Backup wiederherstellen:
cp /config/www/release_data.json.backup /config/www/release_data.json
```

### Problem: "Frontend assets not found"

**Ursache:** HTML-Dateien fehlen in Integration

**Lösung:**
```bash
# Prüfe ob Dateien existieren:
ls -la /config/custom_components/release_notes_manager/*.html

# Falls fehlen: Reinstall via HACS oder manuell
```

### Problem: API 404 Fehler

**Ursache:** Integration nicht gestartet

**Lösung:**
```bash
1. Prüfe HA Logs auf Fehler
2. HA neu starten
3. Logs erneut prüfen
```

### Problem: Leeres Admin-Interface

**Ursache:** Daten nicht migriert oder HA-Storage leer

**Lösung:**
```bash
# Prüfe HA-Storage:
cat /config/.storage/release_notes_manager

# Falls leer aber alte Datei vorhanden:
# → Lösche .migrated Marker und restarte:
rm /config/www/release_data.json.migrated
# HA Neustart → Migration läuft erneut
```

---

## 📊 Technische Details

### Migration-Logik

```python
Migration läuft wenn:
  ✅ HA-Storage existiert nicht
  ✅ Alte Datei existiert
  ✅ Keine .migrated Marker-Datei

Migration überspringt wenn:
  ❌ HA-Storage bereits existiert
  ❌ Alte Datei fehlt
  ❌ .migrated Marker existiert
```

### Frontend-Serving

```python
# v0.4.0 (alt):
/local/release-notes/... → /config/www/release-notes/...
# Dateien werden kopiert

# v0.5.0 (neu):
/release-notes/... → /config/custom_components/release_notes_manager/...
# Dateien direkt aus Integration ausgeliefert
```

### Storage-Location

```python
# v0.4.0 (alt):
/config/www/release_data.json
# Manuelles Backup bei jedem Speichern

# v0.5.0 (neu):
/config/.storage/release_notes_manager
# Automatisches Backup durch HA-Storage-API
```

---

## ✅ Checkliste: Upgrade erfolgreich

- [ ] v0.5.0 via HACS installiert
- [ ] HA neu gestartet
- [ ] Logs zeigen erfolgreiche Migration
- [ ] Admin öffnet unter `/release-notes/release-notes.html`
- [ ] Alle Releases werden angezeigt
- [ ] Speichern funktioniert
- [ ] Dashboard URLs aktualisiert
- [ ] Widget funktioniert
- [ ] Alte `.migrated` Datei existiert (Rollback-Sicherung)

**Wenn alle ✅ → Upgrade erfolgreich!** 🎉

---

## 🆘 Support

Bei Problemen:
1. Logs prüfen (Einstellungen → System → Protokolle)
2. [Issue auf GitHub](https://github.com/atheile-ha/ha-release-notes-manager/issues) erstellen
3. Logs und Fehlermeldungen anhängen

**Wichtig:** `.migrated` Datei NICHT löschen vor erfolgreichem Test!
