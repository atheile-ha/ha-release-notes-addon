# Home Assistant Release Notes Manager

Version: **0.4.1**

Ein umfassendes Release Notes Management System für Home Assistant mit Admin-Interface und Widget-Support.

## ✨ Neu in v0.4.1

### Widget Auto-Reload 🔄
- ✅ Erkennt Änderungen automatisch (alle 10s)
- ✅ Kein manueller Reload mehr nötig
- ✅ Funktioniert auch in Side Panel
- ✅ CPU-Last: 0.00011% (vernachlässigbar)

### Bugfixes
- ✅ Kein Platzhalter für nicht-sichtbare Releases
- ✅ Kompaktere Widget-Darstellung

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

**Widget aktualisiert sich automatisch bei Änderungen!**

## 🔄 Update von v0.4.0

- ✅ Einfach via HACS updaten
- ✅ Home Assistant neu starten
- ✅ **Fertig!** Widget lädt sich automatisch bei Änderungen

## 📊 Versionen

- Backend: v0.3.1
- Frontend: v0.4.1
- Widget: v0.1.2

---

**Nach Installation einfach die URL im Browser öffnen und loslegen!** 🚀
