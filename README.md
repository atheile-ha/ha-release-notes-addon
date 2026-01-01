# Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/atheile-ha/ha-release-notes-manager.svg)](https://github.com/atheile-ha/ha-release-notes-manager/releases)
[![License](https://img.shields.io/github/license/atheile-ha/ha-release-notes-manager.svg)](LICENSE)

Ein umfassendes Release Notes Management System für Home Assistant mit Admin-Interface und Widget-Support.

**Version:** v0.4.2

## 📦 Installation

### Via HACS (Empfohlen)

1. HACS öffnen
2. "Integrationen" → ⋮ → "Benutzerdefinierte Repositorys"
3. Repository hinzufügen:
   - URL: `https://github.com/atheile-ha/ha-release-notes-manager`
   - Kategorie: Integration
4. "Release Notes Manager" suchen und installieren
5. Home Assistant neu starten

## 🚀 Verwendung

### Admin-Version
```
http://DEINE-IP:8123/local/release-notes/release-notes.html
```

### Widget-Version
```
http://DEINE-IP:8123/local/release-notes/release-notes-widget.html
```

**Dashboard-Integration:**
```yaml
type: iframe
url: /local/release-notes/release-notes-widget.html
aspect_ratio: 100%
```

## 🆕 v0.4.2 Fixes

### Admin-Version
- ✅ **localStorage statt API**: Keine 404 Fehler mehr beim Speichern
- ✅ **Direktes Speichern**: Sofortige Persistenz ohne Backend
- ✅ **Bessere Fehlerbehandlung**: Klare Meldungen

### Integration
- ✅ **Update-Fix**: HTML-Dateien werden bei Updates überschrieben
- ✅ **Immer aktuell**: Neueste Version wird immer kopiert

### Widget
- ✅ **Auto-Reload**: Erkennt Änderungen automatisch (10s Intervall)
- ✅ **CPU-Last**: 0.00011% (vernachlässigbar)

Siehe [CHANGELOG.md](CHANGELOG.md) für vollständige Details.

## 📝 Lizenz

MIT License - siehe [LICENSE](LICENSE)

## 👤 Autor

Entwickelt von atheile-ha für Home Assistant Community
