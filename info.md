# Home Assistant Release Notes Manager

Version: **0.4.0**

Ein umfassendes Release Notes Management System für Home Assistant mit Admin-Interface und Widget-Support.

## ✨ Features v0.4.0

### Admin-Version
- ✅ 11 neue UI-Verbesserungen
- ✅ Summary Badges im Release-Header
- ✅ Details ein-/ausklappbar
- ✅ Pagination (10 + "Weitere laden")
- ✅ Farbwähler mit 11 Farben
- ✅ Neuestes Release blau hervorgehoben

### Widget-Version (NEU!)
- ✅ Read-Only Ansicht
- ✅ Auto-Collapse (0-300s konfigurierbar)
- ✅ "Alle Releases anzeigen" / "Nur neuestes Release"
- ✅ Settings-Panel mit ⚙️

## 📦 Nach Installation

**Admin-Version:**
```
http://DEINE-IP:8123/local/release-notes/release-notes.html
```

**Widget-Version:**
```
http://DEINE-IP:8123/local/release-notes/release-notes-widget.html
```

## 🎯 Dashboard-Integration

Füge eine Webseiten-Karte hinzu:

```yaml
type: iframe
url: /local/release-notes/release-notes-widget.html
aspect_ratio: 100%
```

## 🔄 Update von v0.3.x

- ✅ Daten bleiben erhalten (localStorage)
- ✅ Automatisches Kopieren der HTML-Dateien
- ✅ Einfach via HACS updaten

## 📊 Versionen

- Backend: v0.3.1
- Frontend: v0.4.0
- Widget: v0.1.0

---

**Nach Installation einfach die URL im Browser öffnen und loslegen!** 🚀
