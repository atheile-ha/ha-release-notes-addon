# 📝 Home Assistant Release Notes Manager

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

Ein elegantes Tool zur Verwaltung und Anzeige von Release Notes direkt in Home Assistant.

## ✨ Features

- 📋 **Release-Verwaltung** - Versionen, Kategorien, Status-Tracking
- ⚠️ **Known Issues** - Bekannte Probleme dokumentieren und verfolgen
- 🎨 **Dashboard-Widget** - Kompakte Anzeige der neuesten Releases
- 🔍 **Suche & Filter** - Schnell das richtige Release finden
- 🔄 **Auto-Reload** - Widget aktualisiert sich automatisch

**⚠️ Breaking Change:** URLs haben sich geändert!
Wegen internem HA-Cache werden neue Front-Ends in Dashboard und iframe Card für das Widget nicht automatisch geladen. Daher ist bis zur Lösung eine Anpassung der Links auf die aktuelle Version erforderlich

## 🆕 Version 0.5.1

### Bugfixes in dieser Version:

✅ **Zeilenumbrüche funktionieren jetzt!**
- Mehrzeilige Texte in Beschreibungen, Changelogs und Known Issues werden korrekt dargestellt
- Enter-Taste im Eingabefeld erzeugt sichtbare Zeilenumbrüche

✅ **Gelöste Fehler in Badge-Zählung**
- Das Änderungs-Badge zählt jetzt auch gelöste Known Issues mit
- Beispiel: 3 Änderungen + 2 gelöste Bugs = "5 Änderungen"

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
```

**Dashboard-Widget:**
```yaml
type: iframe
url: /release-notes/release-notes-widget.html?=v0.5.1
aspect_ratio: 200%
```

**Admin-Interface:**
```
http://DEINE-IP:8123/release-notes/release-notes.html?=v0.5.1
```

## 📝 Dokumentation

- [INFO.md](INFO.md) - Vollständige Dokumentation
- [CHANGELOG.md](CHANGELOG.md) - Versionshistorie

## 🐛 Support

- [GitHub Issues](https://github.com/atheile-ha/ha-release-notes-manager/issues)
- [Troubleshooting](INFO.md#troubleshooting)

## 📜 Lizenz

MIT License - siehe [LICENSE](LICENSE)

---

**Version:** 0.5.1  
**Repository:** https://github.com/atheile-ha/ha-release-notes-manager
