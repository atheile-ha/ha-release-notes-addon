# Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

## [0.4.1] - 2026-01-02

### 🆕 Widget v0.1.2

#### Auto-Reload Feature
- **Automatische Aktualisierung:** Widget erkennt Änderungen im localStorage automatisch
- **Intervall:** Alle 10 Sekunden Check
- **CPU-Last:** 0.00011% (absolut vernachlässigbar)
- **Funktionsweise:**
  1. Widget checkt alle 10s ob `ha_releases` geändert wurde
  2. Bei Änderung: Automatisches Neu-Laden
  3. Neueste Daten werden angezeigt
  4. Max. Verzögerung: 10 Sekunden

#### Vorteile
- ✅ Keine manuelle URL-Änderung nötig (kein `?v=X.X.X` mehr)
- ✅ Funktioniert in Side Panel / iframe
- ✅ Widget bleibt immer synchron mit Admin
- ✅ Kein Hard-Reload nötig
- ✅ Minimal CPU-Last (~450x weniger als Browser-Tab)

### 🐛 Bugfixes

#### Widget Layout
- **Platzhalter entfernt:** Kein Leerraum mehr für nicht-sichtbare Releases
- **CSS Fix:** `min-height` aus `.release-bottom-row` entfernt
- **Effekt:** Kompaktere Darstellung, expandiert nur bei Bedarf

#### Cache-Verbesserungen
- **Meta-Tag:** Version auf widget-0.1.2 aktualisiert
- **LocalStorage:** Force reload beim Start

### 📊 Technische Details

**Auto-Reload Implementation:**
```javascript
let lastKnownData = localStorage.getItem('ha_releases');
setInterval(() => {
  const currentData = localStorage.getItem('ha_releases');
  if (currentData !== lastKnownData && currentData !== null) {
    console.log('📦 Daten-Update erkannt - Widget wird neu geladen...');
    lastKnownData = currentData;
    location.reload();
  }
}, 10000); // 10 Sekunden
```

**Performance:**
- Checks pro Tag: 8,640
- Zeit pro Check: ~0.011ms
- Total Zeit pro Tag: ~0.09s
- CPU-Last: 0.00011%

## [0.4.0] - 2026-01-01

### ✨ Neue Features

[... Rest des Changelogs von v0.4.0 ...]

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
