# Installation Guide - Release Notes Manager v0.3.0

Vollständige Schritt-für-Schritt Anleitung zur Installation und Konfiguration.

## 📋 Inhaltsverzeichnis

- [Voraussetzungen](#voraussetzungen)
- [Installation via HACS](#installation-via-hacs)
- [Manuelle Installation](#manuelle-installation)
- [Konfiguration](#konfiguration)
- [Erster Start](#erster-start)
- [Dashboard Integration](#dashboard-integration)
- [Verifikation](#verifikation)
- [Troubleshooting](#troubleshooting)

---

## Voraussetzungen

Stelle sicher, dass folgendes erfüllt ist:

- ✅ Home Assistant **2024.1.0 oder neuer**
- ✅ HACS installiert (für HACS-Installation)
- ✅ Zugriff auf `configuration.yaml`
- ✅ Neustart-Berechtigung für Home Assistant

---

## Installation via HACS

### Schritt 1: Repository hinzufügen

1. **Öffne HACS** in Home Assistant
2. Klicke auf **Integrationen**
3. Klicke auf die **drei Punkte** ⋮ oben rechts
4. Wähle **"Benutzerdefinierte Repositories"**
5. Füge hinzu:
   - **Repository:** `https://github.com/your-username/ha-release-notes-manager`
   - **Kategorie:** `Integration`
6. Klicke **"Hinzufügen"**

### Schritt 2: Integration installieren

1. Suche in HACS nach **"Release Notes Manager"**
2. Klicke auf die Integration
3. Klicke **"Herunterladen"**
4. Warte bis Download abgeschlossen ist
5. Du siehst eine Bestätigung: "Download erfolgreich"

### Schritt 3: Home Assistant neu starten

**WICHTIG:** Nach HACS-Installation ist ein **vollständiger Neustart** erforderlich:

1. Gehe zu **Einstellungen → System**
2. Klicke **"Neu starten"**
3. Bestätige mit **"Neu starten"**
4. Warte bis Home Assistant vollständig hochgefahren ist (ca. 1-2 Minuten)

---

## Manuelle Installation

### Schritt 1: Download

1. Gehe zu [GitHub Releases](https://github.com/your-username/ha-release-notes-manager/releases)
2. Lade die neueste Version herunter (`release_notes_manager-0.3.0.zip`)
3. Entpacke das Archiv

### Schritt 2: Dateien kopieren

**Via SSH/Terminal:**

```bash
# Navigiere zum Home Assistant config Verzeichnis
cd /config

# Erstelle Verzeichnis falls nicht vorhanden
mkdir -p custom_components

# Kopiere den entpackten Ordner
cp -r /path/to/extracted/release_notes_manager custom_components/
```

**Via File Editor Add-on:**

1. Öffne File Editor
2. Erstelle Ordner: `custom_components/release_notes_manager`
3. Lade folgende Dateien hoch:
   - `__init__.py`
   - `manifest.json`
   - `api.py`
4. Erstelle Unterordner: `www`
5. Lade hoch: `index.html`

### Schritt 3: Struktur verifizieren

Prüfe dass folgende Struktur existiert:

```
/config/custom_components/release_notes_manager/
├── __init__.py
├── manifest.json
├── api.py
└── www/
    └── index.html
```

**Via Terminal prüfen:**

```bash
ls -la /config/custom_components/release_notes_manager/
ls -la /config/custom_components/release_notes_manager/www/
```

### Schritt 4: Home Assistant neu starten

Wie bei HACS-Installation: **Einstellungen → System → Neu starten**

---

## Konfiguration

### Schritt 1: configuration.yaml bearbeiten

Öffne deine `configuration.yaml` und füge hinzu:

```yaml
# Release Notes Manager
release_notes_manager:
```

**Hinweis:** Keine weiteren Optionen erforderlich. Die Integration läuft mit Standardeinstellungen.

### Schritt 2: Konfiguration neu laden

Nach dem Bearbeiten von `configuration.yaml`:

**Option A: Neustart (empfohlen bei Erstinstallation)**

1. **Einstellungen → System → Neu starten**
2. Warte bis HA vollständig hochgefahren ist

**Option B: YAML-Konfiguration neu laden (schneller)**

1. **Einstellungen → System → YAML-Konfiguration neu laden**
2. Wähle **"Alle YAML-Konfigurationen neu laden"**
3. Warte auf Bestätigung

**Unterschied:**

- **Neustart:** Lädt alle Komponenten neu (1-2 Min)
- **YAML neu laden:** Nur Konfiguration (10-30 Sek)

**Empfehlung für v0.3.0 Erstinstallation:** ✅ **Neustart**

---

## Erster Start

### Schritt 1: Logs prüfen

1. Gehe zu **Einstellungen → System → Protokolle**
2. Suche nach `release_notes_manager`
3. Du solltest sehen:

```
[custom_components.release_notes_manager] Release Notes Manager initialized
[custom_components.release_notes_manager.api] Release Notes API registered
[custom_components.release_notes_manager] Static files registered at /local/release-notes/
```

**Falls Fehler auftreten:** Siehe [Troubleshooting](#troubleshooting)

### Schritt 2: Anwendung öffnen

Öffne in deinem Browser:

```
http://DEINE-HA-IP:8123/local/release-notes/release-notes.html
```

**Ersetze `DEINE-HA-IP` mit:**
- Deiner Home Assistant IP-Adresse (z.B. `192.168.1.100`)
- Oder `homeassistant.local` (wenn mDNS funktioniert)

**Beispiele:**
```
http://192.168.1.100:8123/local/release-notes/release-notes.html
http://homeassistant.local:8123/local/release-notes/release-notes.html
```

### Schritt 3: Erste Schritte

Du solltest sehen:
- ✅ Home Assistant Logo
- ✅ Titel: "Home Assistant Release Notes Manager"
- ✅ Buttons: "⚙ Kategorien" und "+ Neues Release"
- ✅ Leere Release-Liste: "Keine Releases - Erstelle dein erstes Release!"

---

## Dashboard Integration

### Option 1: iFrame Card (empfohlen)

**UI-Editor:**

1. Dashboard öffnen
2. Rechts oben: Bearbeiten
3. "+ Karte hinzufügen"
4. Suche nach "Webseite"
5. Konfiguriere:
   - **URL:** `/local/release-notes/release-notes.html`
   - **Seitenverhältnis:** `100%`
6. Speichern

**YAML-Editor:**

```yaml
type: iframe
url: /local/release-notes/release-notes.html
aspect_ratio: 100%
```

### Option 2: Dedicated View

Erstelle ein eigenes Tab im Dashboard:

```yaml
views:
  - title: Release Notes
    path: releases
    icon: mdi:notebook
    cards:
      - type: iframe
        url: /local/release-notes/release-notes.html
        aspect_ratio: 100%
```

### Option 3: Panel (Vollbild)

Für Vollbild-Ansicht:

```yaml
views:
  - title: Release Notes
    path: releases
    panel: true
    cards:
      - type: iframe
        url: /local/release-notes/release-notes.html
```

---

## Verifikation

### Checkliste nach Installation

- [ ] **Integration geladen**
  - Logs zeigen "Release Notes Manager initialized"
  - Keine Fehler in den Logs
  
- [ ] **Dateien registriert**
  - `/local/release-notes/release-notes.html` erreichbar
  - Seite lädt ohne 404-Fehler
  
- [ ] **UI funktioniert**
  - Logo wird angezeigt
  - Buttons sind klickbar
  - Modal öffnet sich
  
- [ ] **Speichern funktioniert**
  - Release erstellen
  - Speichern klicken
  - Bestätigung: "✅ Gespeichert!"
  - Datei `/config/www/release_data.json` existiert
  
- [ ] **Persistenz**
  - Browser neu laden (Strg+Shift+R)
  - Release ist noch da
  
- [ ] **Backup**
  - Datei `/config/www/release_data.json.backup` existiert

### Automatischer Test

Öffne Browser Console (F12) und prüfe:

```javascript
// Sollte zeigen:
🚀 Home Assistant Release Notes Manager v0.3.0-CORRECTED startet...
📥 Lade Daten...
✅ Geladen: {...}
```

---

## Troubleshooting

### Problem: Integration nicht gefunden

**Symptom:** Logs zeigen nichts über release_notes_manager

**Lösung:**

1. Prüfe `configuration.yaml`:
   ```yaml
   release_notes_manager:  # ← Korrekt?
   ```

2. Prüfe Dateien:
   ```bash
   ls -la /config/custom_components/release_notes_manager/
   ```
   Sollte zeigen: `__init__.py`, `manifest.json`, `api.py`, `www/`

3. **Vollständiger Neustart** (nicht nur YAML reload)

4. Prüfe Logs auf Fehler

### Problem: 404 Not Found

**Symptom:** `/local/release-notes/release-notes.html` zeigt 404

**Lösung:**

1. Prüfe dass Datei existiert:
   ```bash
   ls -la /config/custom_components/release_notes_manager/www/index.html
   ```

2. Prüfe Logs:
   ```
   Static files registered at /local/release-notes/
   ```

3. **Neustart** Home Assistant

4. Browser-Cache leeren:
   - **Chrome/Edge:** Strg+Shift+Delete
   - **Firefox:** Strg+Shift+Delete
   - Oder einfach: Strg+Shift+R (Hard Reload)

### Problem: Speichern fehlgeschlagen

**Symptom:** Alert "Speichern fehlgeschlagen!"

**Lösung:**

1. Browser Console öffnen (F12)
2. Prüfe Fehlermeldung
3. Prüfe Logs in Home Assistant
4. Prüfe Schreibrechte:
   ```bash
   ls -la /config/www/
   ```
5. Erstelle Verzeichnis falls nicht vorhanden:
   ```bash
   mkdir -p /config/www
   chmod 755 /config/www
   ```

### Problem: Leere Seite

**Symptom:** Seite lädt aber zeigt nichts

**Lösung:**

1. Browser Console (F12) öffnen
2. Prüfe auf JavaScript-Fehler
3. Hard Reload: **Strg+Shift+R**
4. Andere Browser testen
5. Datei neu herunterladen

### Problem: HACS zeigt Integration nicht

**Symptom:** Integration nicht in HACS sichtbar

**Lösung:**

1. Repository URL korrekt eingegeben?
2. Kategorie "Integration" gewählt?
3. HACS neu laden:
   ```
   HACS → ⋮ → Repositories neu laden
   ```
4. Warte 1-2 Minuten
5. Suche erneut

---

## Deinstallation

Falls du die Integration entfernen möchtest:

### Schritt 1: Aus configuration.yaml entfernen

Lösche die Zeile:
```yaml
release_notes_manager:  # ← Diese Zeile löschen
```

### Schritt 2: Integration entfernen

**Via HACS:**
1. HACS → Integrationen
2. Release Notes Manager
3. ⋮ → Entfernen

**Manuell:**
```bash
rm -rf /config/custom_components/release_notes_manager
```

### Schritt 3: Daten löschen (optional)

Wenn du auch die Daten löschen möchtest:

```bash
rm /config/www/release_data.json
rm /config/www/release_data.json.backup
```

### Schritt 4: Neustart

**Einstellungen → System → Neu starten**

---

## Updates

### Via HACS

1. HACS → Integrationen
2. Suche Updates
3. Falls Update verfügbar: "Aktualisieren"
4. **Neustart** Home Assistant

### Manuell

1. Download neue Version
2. Ersetze Dateien in `/config/custom_components/release_notes_manager/`
3. **Neustart** Home Assistant

**Hinweis:** Deine Daten in `/config/www/release_data.json` bleiben erhalten!

---

## Support

Bei Problemen:

1. ✅ Prüfe [Troubleshooting](#troubleshooting)
2. ✅ Prüfe [GitHub Issues](https://github.com/your-username/ha-release-notes-manager/issues)
3. ✅ Erstelle neues Issue mit:
   - Home Assistant Version
   - Browser & Version
   - Fehlermeldung
   - Logs (HA + Browser Console)

---

**Installation erfolgreich? [→ Zurück zur README](README.md)**
