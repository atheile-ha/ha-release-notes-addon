# Changelog

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
- ✅ **Empfehlung:** Nutze `?` am URL-Ende für Dashboard (verhindert Browser-Cache)

**Widget-Layout:**
- ✅ min-height aus .release-bottom-row entfernt
- ✅ Kein Leerraum mehr für nicht-sichtbare Releases
- ✅ **Empfehlung:** aspect_ratio: 200% für optimale Darstellung

## [0.3.1] - 2024-12-15

### Backend-Version (unverändert in v0.4.0)

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
