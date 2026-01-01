# Changelog

## [0.4.2] - 2026-01-02

### 🐛 Kritische Bugfixes

#### Admin-Version: localStorage statt API
**Problem:** Admin zeigte "Speichern fehlgeschlagen" mit API 404 Fehler

**Ursache:**
- saveData() versuchte zu speichern über `/api/release_notes_manager/save`
- API existiert nicht (nur localStorage-basierte Lösung)
- loadData() versuchte `/local/release_data.json` zu laden

**Lösung:**
```javascript
// VORHER
async function saveData() {
  const r = await fetch('/api/release_notes_manager/save', {...});
  // API 404 Error!
}

// NACHHER  
function saveData() {
  localStorage.setItem('ha_releases', JSON.stringify(state.releases));
  localStorage.setItem('ha_categories', JSON.stringify([...state.categories]));
  // Funktioniert perfekt!
}
```

**Änderungen:**
- ✅ `loadData()`: localStorage statt fetch()
- ✅ `saveData()`: localStorage statt API call
- ✅ Keine API 404 Fehler mehr
- ✅ Sofortiges Speichern ohne Backend
- ✅ Status-Text: "Daten werden lokal gespeichert"

#### Integration: Update-Fix

**Problem:** HTML-Dateien wurden bei Updates nicht überschrieben

**Ursache in `__init__.py`:**
```python
# VORHER
if source.exists() and not target.exists():
    shutil.copy(source, target)
# Kopiert NUR wenn Datei NICHT existiert
# Bei Update: Alte Dateien bleiben!
```

**Lösung:**
```python
# NACHHER
if source.exists():
    shutil.copy2(source, target)  # IMMER kopieren
    _LOGGER.info("Copied %s (updated)", filename)
```

**Effekt:**
- ✅ HTML-Dateien werden bei jedem HA-Start aktualisiert
- ✅ Updates funktionieren zuverlässig
- ✅ Immer neueste Version aktiv

### 📊 Versionen

- **Admin:** v0.4.2 (localStorage-fix)
- **Widget:** v0.1.2 (Auto-Reload)  
- **Integration:** v0.4.2 (Update-fix)

## [0.4.1] - 2026-01-02

### 🆕 Widget v0.1.2 - Auto-Reload Feature
[... siehe vorheriges Changelog ...]

## [0.4.0] - 2026-01-01

### ✨ Neue Features (11 Features)
[... siehe vorheriges Changelog ...]

---

**Legende:**
- ✨ Neue Features  
- 🔧 Verbesserungen
- 🐛 Bugfixes
- 🏗️ Technische Änderungen
