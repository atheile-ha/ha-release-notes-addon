# 📝 Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

Ein elegantes Tool zur Verwaltung und Anzeige von Release Notes direkt in Home Assistant.

## ✨ Features

- 📋 **Release-Verwaltung** - Versionen, Kategorien, Status-Tracking
- ⚠️ **Known Issues** - Bekannte Probleme dokumentieren, verfolgen und beim nächsten Release automatisch übernehmen
- 🎨 **Admin-Interface (Eingabe-Dashboard)** - Vollständiges Verwaltungs-Interface zum Erstellen und Bearbeiten von Releases
- 🖥️ **Dashboard-Widget (Read-only-Dashboard)** - Kompakte Anzeige der neuesten Releases
- 🔍 **Suche & Filter** - Schnell das richtige Release finden
- 🔄 **Auto-Reload** - Beide Dashboards prüfen ihre jeweilige Version gegen das Backend
- 🔧 **Einstellungen** - Popup im Admin-Interface, u.a. mit Export/Import des Datenstands als JSON
- 🖱️ **Drag'n'Drop** - Einträge im Admin-Interface zwischen "Neue Features" und "Änderungen/Bugfixes" verschieben und innerhalb eines Bereichs umsortieren
- 🔄 **Automatische Update-Dokumentation** - Beobachtet alle `update.*`-Entitäten der Instanz und legt bei abgeschlossenen Updates sowie neu hinzugekommenen/entfernten Integrationen automatisch passende Release-Notes-Einträge an (ein-/ausschaltbar in den Einstellungen)

**⚠️ Wichtiger Hinweis zu Dashboard-URLs**

Home Assistant cached Dashboard-Kacheln (Dashboard-Tab und iframe-Card) intern und lädt ein aktualisiertes Front-End nicht automatisch nach. Deshalb wird in den URLs unten ein `?=vX.X.X`-Parameter mit der aktuellen Admin- bzw. Widget-Version mitgegeben - nach einem Update muss dieser Parameter manuell angepasst werden (siehe [Troubleshooting](#-troubleshooting)).

## 🆕 Version 0.6.1

### Neu in dieser Version:

✅ **Automatische Update-Dokumentation über Home-Assistant-Update-Entitäten** (v0.6.0)
- Abgeschlossene Updates werden automatisch als Eintrag `"[alte Version] → [neue Version]"` in der Kategorie "Update" dokumentiert
- Neu hinzukommende bzw. verschwindende `update.*`-Entitäten (Integration/Add-on installiert bzw. deinstalliert) werden ebenfalls automatisch erfasst
- Erkennung funktioniert zuverlässig auch bei Updates, die einen HA-Neustart erfordern
- Ein-/ausschaltbar über den neuen Bereich "🔄 Automatische Update-Dokumentation" in den Einstellungen (⚙️) des Admin-Interfaces

🐛 **Bugfix (v0.6.1):** Entitäten, deren Version beim HA-Start noch nicht bekannt war, lösten fälschlich einen `"? → ..."`-Eintrag aus, sobald ihr erster echter Wert eintraf. Das wird jetzt korrekt als bloßes Nachtragen der Baseline erkannt, ohne Eintrag.

Vollständige Versionshistorie: [CHANGELOG.md](CHANGELOG.md)

## 🏗️ Architektur

- **HA-Storage basiert:** Daten werden in Home Assistant's offiziellem Storage-System (`/config/.storage/release_notes_manager`) gespeichert
- **Frontend-Serving direkt aus der Integration:** kein Kopieren nach `/config/www/` nötig, URLs unter `/release-notes/`
- **API:** `GET`/`POST /api/release_notes_manager/data` zum Laden/Speichern, `GET /api/release_notes_manager/version` liefert die aktuellen Versionsstände von Backend, Admin- und Widget-Dashboard
- **Drei unabhängige Versionsstände:** Backend, Admin-Dashboard (`release-notes.html`) und Widget-Dashboard (`release-notes-widget.html`) haben jeweils eigene Versionsnummern, die nur erhöht werden, wenn an genau dieser Datei etwas geändert wurde. Die Paketversion in `manifest.json`/`hacs.json` wird davon unabhängig bei jedem Release hochgezählt.

## 🚀 Installation

### Via HACS (empfohlen)

1. HACS öffnen
2. Menü (⋮) → "Benutzerdefinierte Repositories"
3. Repository: `https://github.com/atheile-ha/ha-release-notes-manager`
4. Kategorie: **Integration**
5. "Release Notes Manager" installieren
6. Home Assistant neu starten

### Manuelle Installation

1. Kopiere `custom_components/release_notes_manager` nach `/config/custom_components/`
2. Home Assistant neu starten

## ⚙️ Konfiguration

**configuration.yaml:**
```yaml
release_notes_manager:

# Optional: Debug-Logging
logger:
  default: info
  logs:
    custom_components.release_notes_manager: debug
```

**Dashboard-Widget (iframe-Card):**
```yaml
type: iframe
url: /release-notes/release-notes-widget.html?=v0.5.3
aspect_ratio: 200%
```

**Admin-Interface als Dashboard-Tab:**
```yaml
title: Release Notes
icon: mdi:note-text
url: /release-notes/release-notes.html?=v0.6.0
```

**Admin-Interface direkt im Browser:**
```
http://DEINE-IP:8123/release-notes/release-notes.html?=v0.6.0
```

Die Versionsnummer im `?=vX.X.X`-Parameter muss zur jeweils aktuellen **Widget**- bzw. **Admin**-Version passen (nicht zur Backend- oder Paketversion) - siehe [CHANGELOG.md](CHANGELOG.md).

## 📖 Verwendung

### Release erstellen

1. Admin-Interface öffnen (`/release-notes/release-notes.html`)
2. **"+ Neues Release"** klicken
3. Formular ausfüllen:
   - Version (z.B. "2025.1.0")
   - Name (optional)
   - Datum
   - Features, Änderungen/Bugfixes, bekannte Fehler
4. **"Speichern"** klicken

### Known Issue hinzufügen

1. Release öffnen (✏️)
2. Zu **"Bekannte Fehler"** scrollen
3. **"+ Hinzufügen"** klicken
4. Titel und Details eingeben
5. **"Speichern"**

Offene bekannte Fehler werden beim Anlegen eines neuen Release automatisch als Vorschlag übernommen und können dort als gelöst markiert werden.

### Kategorien verwalten

1. Oben rechts **"Kategorien"** klicken
2. Neue Kategorie hinzufügen oder bestehende bearbeiten
3. Farbe anpassen (Klick auf das Label)

### Automatische Update-Dokumentation

Läuft standardmäßig aktiviert im Hintergrund und benötigt keine Konfiguration:

- Schließt eine `update.*`-Entität in Home Assistant ein Update ab, wird automatisch ein Eintrag `"[alte Version] → [neue Version]"` in der Kategorie **"Update"** im passenden Tages-Release angelegt (neues Release wird bei Bedarf automatisch erstellt, Versionsschema `YYYY.M.N`)
- Neu hinzugekommene bzw. entfernte `update.*`-Entitäten werden als **"Neuinstallation"**/**"Deinstallation"** in der Kategorie **"Integration / Addon"** dokumentiert
- Mehrere gleichzeitige Ereignisse werden zu einer gemeinsamen Benachrichtigung gebündelt (Home Assistant → Mitteilungen)
- Beim ersten Aktivieren wird nur eine stille Bestandsaufnahme durchgeführt, es entstehen keine rückwirkenden Einträge für bereits installierte Komponenten

**Ein-/Ausschalten:** Admin-Interface → ⚙️ **Einstellungen** → Abschnitt "🔄 Automatische Update-Dokumentation"

## 🐛 Troubleshooting

### Releases werden nicht angezeigt / Dashboard zeigt eine alte Version

**Lösung 1: Versionsnummer in der Dashboard-URL prüfen**

Die URL muss die aktuelle Admin-/Widget-Version referenzieren (siehe [Konfiguration](#️-konfiguration)), sonst liefert Home Assistant eine gecachte, alte Kachel aus.

**Lösung 2: Browser-Cache leeren**
```
Strg + Shift + R (Hard Reload)
```

**Lösung 3: Logs prüfen**
```
Einstellungen → System → Protokolle
Suche: "release_notes_manager"
```

### 404 Error beim Öffnen

**URL prüfen:**
- ✅ Richtig: `/release-notes/release-notes.html?...`
- ❌ Falsch: `/local/release-notes/...` (alte URL-Struktur vor v0.5.0)

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

## 🤝 Support

- [GitHub Issues](https://github.com/atheile-ha/ha-release-notes-manager/issues)
- [Troubleshooting](#-troubleshooting)

## 📜 Lizenz

MIT License - siehe [LICENSE](LICENSE)

---

Entwickelt für die Home Assistant Community 🏠

**Version:** 0.6.1  
**Repository:** https://github.com/atheile-ha/ha-release-notes-manager
