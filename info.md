# Home Assistant Release Notes Manager

Version: **0.4.0**

Release Notes Management System mit Admin-Interface und Widget-Support.

## ✨ Neu in v0.4.0

### 11 Frontend Features
- ✅ Delete-Button mit Icon 🗑️
- ✅ Kategorie-Icons & Color-Picker
- ✅ Summary Badges im Header
- ✅ Neuestes Release hervorgehoben (Blau)
- ✅ Details Toggle (▶/▼)
- ✅ Pagination ("Weitere laden")
- ✅ Version Footer

### Widget v0.1.2
- ✅ Auto-Reload (erkennt Änderungen alle 10s)
- ✅ Kein Platzhalter mehr
- ✅ CPU-Last: 0.00011%

### Fixes
- ✅ Cache-Problem behoben
- ✅ Updates funktionieren zuverlässig

## 📦 Nach Installation

**Admin:** `/local/release-notes/release-notes.html?`  
**Widget:** `/local/release-notes/release-notes-widget.html?`

**Tipp:** Das `?` verhindert Browser-Cache!

## 🎯 Dashboard-Integration

```yaml
type: iframe
url: /local/release-notes/release-notes-widget.html?
aspect_ratio: 200%
```

**Widget aktualisiert sich automatisch bei Änderungen!**

## 🔄 Update von v0.3.1

- ✅ Einfach via HACS updaten
- ✅ Home Assistant neu starten
- ✅ **Daten bleiben erhalten!**
- ✅ Backend 100% kompatibel

## 📊 Versionen

- Backend: v0.3.1 (unverändert)
- Frontend: v0.4.0 (11 neue Features)
- Widget: v0.1.2 (Auto-Reload)

---

**11 neue Features + Widget + Alle Fixes!** 🚀
