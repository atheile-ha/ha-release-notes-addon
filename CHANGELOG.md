# Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

## [0.4.0] - 2026-01-01

### ✨ Neue Features

#### Features 1-11 (Änderungen)

**Feature 1: Löschen-Button im Modal**
- Roter "Release vollständig löschen" Button am Ende des Bearbeitungs-Modals
- Direktes Löschen ohne Umwege

**Feature 2: Pencil Icon**
- Stift-Symbol ✏️ statt "Bearbeiten"-Text
- Kompakteres Design
- Tooltip: "Release bearbeiten"

**Feature 3: Zahnrad-Symbol**
- ⚙️ statt "Kategorien verwalten"-Text im Header
- Konsistentes Icon-Design
- Tooltip: "Kategorien verwalten"

**Feature 4: Alphabetische Sortierung**
- Alle Kategorien-Dropdowns alphabetisch sortiert (6 Stellen)
- Deutsche Sortierung mit `localeCompare('de')`
- Umlaute korrekt sortiert

**Feature 5: Farbwähler**
- 11 Farben: Grau, Rot, Orange, Gelb, Grün, Türkis, Blau, Indigo, Lila, Pink, Rose
- Dynamisches Popup beim Klick auf Kategorie-Badge
- Intelligente Positionierung (above/below je nach Platz)
- Click-Outside schließt Popup

**Feature 6: Neue Einträge oben**

**Feature 7: Einheitliche Badge-Ausrichtung**

**Feature 8: Blauer Header für neuestes Release**
- Erstes Release in Liste mit blauem Hintergrund

**Feature 9: Summary Badges im Header**
- Drei Badges im Release-Header:
  - 🟢 Grün: Features (1 Feature / 2 Features)
  - 🔵 Blau: Änderungen (1 Änderung / 2 Änderungen)
  - 🟡 Gelb: Fehler (nur offene, nicht resolved)

**Feature 10: Details ein-/ausklappbar**
- "▶ Details anzeigen" / "▼ Ausblenden" Links
- Für Features, Änderungen und Bekannte Fehler
- Details standardmäßig eingeklappt
- Klick öffnet/schließt Details

**Feature 11: Pagination**
- Initial 10 neueste Releases angezeigt
- "Weitere Releases laden" Button
- +10 Releases pro Klick
- Button verschwindet wenn alle geladen
- Suche durchsucht ALLE Releases (keine Pagination bei Suche)
- Button-Design: Weißer Hintergrund, abgerundet, Schatten

### 🎨 Widget v0.1.0 (NEU!)

#### Read-Only Widget
- Komplett neue Widget-Version ohne Edit-Funktionen
- Nutzt gleichen localStorage wie Admin-Version
- Änderungen im Admin sofort im Widget sichtbar

#### Auto-Collapse Funktion
- Konfigurierbar: 0 (Aus), 10-300 Sekunden
- Slider mit 10s-Schritten
- Anzeige: "30s" oder "Aus" bei 0
- Timer startet bei "Alle Releases anzeigen"
- Timer stoppt bei Expand anderer Releases
- Timer startet neu bei Collapse
- Nach Ablauf: Nur neuestes Release sichtbar

#### Smart Display Logic
- Initial: Nur neuestes Release expanded
- Details trotzdem zugeklappt
- "Alle Releases anzeigen" Button lädt ALLE auf einmal
- "Nur neuestes Release" Button zurück zur Einzelansicht

#### Settings-Panel
- ⚙️ Button oben rechts
- Ausklappbares Panel
- Slider: 0-300 Sekunden
- Live-Anzeige der eingestellten Zeit
- Blauer Hintergrund, kompaktes Design

#### Buttons
- "Alle Releases anzeigen" - Weißer Hintergrund, abgerundet
- "Nur neuestes Release" - Blauer Text, Hover-Effekt
- Beide mit abgerundeten Ecken und Hover-Hintergrund

### 🔧 Verbesserungen

**Cache-Busting**
- Meta-Tags für automatische Browser-Updates
- `Cache-Control: no-cache, no-store, must-revalidate`
- `Pragma: no-cache`
- `Expires: 0`
- Version im Meta-Tag

**Versionsanzeige**
- Unten links: "Backend: v0.3.1 | Frontend: v0.4.0"
- Widget: "Backend: v0.3.1 | Widget: v0.1.0"


## [0.3.1] - Backend

Aktuelle Backend-Version (unverändert).

---

**Legende:**
- ✨ Neue Features
- 🔧 Verbesserungen
- 🐛 Bugfixes
- 🏗️ Technische Änderungen
- 📦 Dateien
- ⚠️ Breaking Changes
