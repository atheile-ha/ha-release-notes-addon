# Release v0.3.2 - UI/UX Improvements

**Release Date:** December 16, 2024  
**Type:** Feature Release  
**Breaking Changes:** None

Dieses Release kombiniert geplante Features aus v0.3.2 und v0.3.3 der Roadmap mit Fokus auf UI/UX Verbesserungen.

## ✨ Neue Features

### Zusammenfassung in Übersicht
Releases zeigen jetzt in der minimierten Ansicht eine Zusammenfassung:
- X Features
- X Änderungen  
- X offene Bugs
- X gelöste Bugs

Schneller Überblick über den Umfang eines Releases!

### Markdown Export
Exportiere einzelne Releases als Markdown-Datei (.md):
- Perfekt für GitHub Releases
- Ideal für Dokumentation
- Praktisch als Backup

Einfach im Release-Menü "Export MD" klicken.

### Keyboard Shortcuts
Arbeite schneller mit Tastatur-Shortcuts:
- **Strg+S** - Speichern
- **ESC** - Modals schließen

### Dark Mode
Automatische Unterstützung für Dark Mode basierend auf System-Einstellung. Keine Konfiguration nötig!

### Alphabetische Sortierung
Kategorien werden jetzt alphabetisch sortiert in allen Dropdowns angezeigt.

### Verbesserte Usability
- Neue Einträge erscheinen **oben** in der Liste (statt unten)
- **Pencil Icon (✏️)** statt "Bearbeiten" Button (platzsparender)
- **Löschen-Button** nur noch im Edit-Modus sichtbar
- **Loading Indicator** beim Speichern mit Feedback

## 🐛 Bugfixes

### HACS Validation Error behoben
Der "brands" Validation-Fehler ist behoben. Repository kann jetzt problemlos als Custom Integration hinzugefügt werden.

## 📦 Installation

### Via HACS (Empfohlen)
1. HACS → ⋮ → Benutzerdefinierte Repositories
2. URL: `https://github.com/atheile-ha/ha-release-notes-addon`
3. Kategorie: Integration
4. Suchen → Download
5. Home Assistant neu starten

### Update von v0.3.0/v0.3.1
1. HACS → Release Notes Manager → Update
2. Home Assistant neu starten
3. Daten bleiben erhalten! ✅

### Manuell
Download: [release_notes_manager-0.3.2.zip](https://github.com/atheile-ha/ha-release-notes-addon/releases/download/v0.3.2/release_notes_manager-0.3.2.zip)

```bash
# Entpacken nach:
/config/custom_components/release_notes_manager/

# Home Assistant neu starten
```

## 🔄 Upgrade Notes

**Kompatibilität:**
- ✅ Voll kompatibel mit v0.3.0 und v0.3.1
- ✅ Keine Datenmodell-Änderungen
- ✅ Automatische Datenmigration nicht erforderlich
- ✅ Rollback auf v0.3.1 problemlos möglich

**Deine Daten:**
- ✅ Alle Releases bleiben erhalten
- ✅ Alle Kategorien bleiben erhalten
- ✅ Alle bekannten Fehler bleiben erhalten
- ✅ Kein manuelles Eingreifen nötig

## 🎯 Quick Start

Nach dem Update:
1. Öffne die Anwendung wie gewohnt
2. Probiere **Strg+S** zum Speichern
3. Teste **Markdown Export** bei einem Release
4. Genieße **Dark Mode** (wenn System auf dark gestellt)
5. Beachte **Zusammenfassung** in minimierten Releases

## 📊 Technische Details

**Änderungen:**
- Frontend: ~50 Zeilen neuer Code
- Backend: Keine Änderungen
- Datenmodell: Keine Änderungen
- API: Keine Änderungen

**Dateigröße:**
- HTML: ~30 KB (war ~26 KB)
- Gesamt-Integration: ~35 KB

**Performance:**
- Keine messbaren Performance-Unterschiede
- Ladezeit: < 100ms (wie bisher)

## 🧪 Getestet mit

- ✅ Home Assistant 2024.12.x
- ✅ Chrome 120+
- ✅ Firefox 121+
- ✅ Safari 17+
- ✅ Edge 120+
- ✅ Mobile (iOS & Android)

## 🔗 Links

- [Repository](https://github.com/atheile-ha/ha-release-notes-addon)
- [Issues](https://github.com/atheile-ha/ha-release-notes-addon/issues)
- [CHANGELOG](CHANGELOG.md)
- [README](README.md)

## 💬 Feedback

Probleme oder Vorschläge? Erstelle ein [Issue](https://github.com/atheile-ha/ha-release-notes-addon/issues)!

---

**Was kommt als nächstes?**  
Roadmap: Export/Import Features, Widget-Modus, HA Sensor-Integration

Siehe [Feature Roadmap](https://github.com/atheile-ha/ha-release-notes-addon/wiki) für Details.
