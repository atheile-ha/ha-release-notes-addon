# Home Assistant Release Notes Manager

Eine professionelle Web-Anwendung zur Verwaltung von Release Notes direkt in Home Assistant.

## ✨ Highlights

- 📝 **Release-Verwaltung** - Versionierte Releases mit Features, Changes und Known Issues
- 🎯 **Intelligentes Fehler-Management** - Automatische Übernahme offener Fehler in neue Releases
- 🏷️ **Kategorisierung** - 6 vordefinierte + eigene Kategorien mit Farbcodierung
- 🔍 **Suche & Filter** - Finde Releases schnell und einfach
- 📱 **Responsive Design** - Funktioniert auf Desktop, Tablet und Mobile
- 🚀 **100% Offline** - Keine Internetverbindung erforderlich
- ⚡ **Schnell & Leicht** - Nur 26 KB, lädt in < 100ms

## 🎯 Perfekt für

- Smart Home Enthusiasten die ihre Änderungen dokumentieren wollen
- Professionelle Home Assistant Setups mit vielen Automationen
- Teams die ihre HA-Installation gemeinsam verwalten
- Dokumentation von Integrations-Updates und -Anpassungen

## 📋 Hauptfunktionen

### Release-Verwaltung
- Releases erstellen, bearbeiten und löschen
- Versionsnummer + optionaler Name
- Expandierbare Release-Cards

### Kategorisierte Einträge
- ✨ **Neue Features** separat dokumentieren
- 🔄 **Änderungen / Bugfixes** übersichtlich darstellen
- ⚠️ **Bekannte Fehler** professionell tracken
- 🏷️ Farbcodierte Kategorien: Allgemein, Heizung, Energie, Automation, Gerät, Integration

### Intelligentes Fehler-Management
- **Automatische Übernahme** offener Fehler in neue Releases
- **Fehler als gelöst markieren** mit Lösungsbeschreibung
- **Gelöste Fehler** erscheinen automatisch in Changes
- **Historie bleibt erhalten** - gelöste Fehler bleiben sichtbar
- **Wieder öffnen** - gelöste Fehler können reaktiviert werden

### Benutzerfreundlichkeit
- Suchfunktion über alle Releases
- Filter nach Kategorien
- Inline-Bearbeitung
- Automatisches Speichern
- Keyboard-Support

## 🔧 Installation

Nach der Installation über HACS:

1. Füge zu `configuration.yaml` hinzu:
   ```yaml
   release_notes_manager:
   ```

2. **Home Assistant neu starten**

3. Öffne die Anwendung:
   ```
   http://DEINE-HA-IP:8123/local/release-notes/release-notes.html
   ```

4. Optional: Als iFrame in Lovelace Dashboard:
   ```yaml
   type: iframe
   url: /local/release-notes/release-notes.html
   aspect_ratio: 100%
   ```

## 📊 Technische Details

- **Anforderung:** Home Assistant 2024.1.0+
- **Dateigröße:** 26 KB
- **Dependencies:** Keine
- **Offline:** Ja
- **Browser:** Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

## 💡 Beispiel-Workflow

1. **Release erstellen**: "2024.12.1 - Weihnachts-Release"
2. **Features hinzufügen**: "Neue PWM-Heizungssteuerung"
3. **Fehler dokumentieren**: "Dashboard lädt langsam"
4. **Nächstes Release**: Fehler wird automatisch übernommen
5. **Fehler lösen**: "Als gelöst markieren in 2024.12.2"
6. **Ergebnis**: Fehler erscheint automatisch in Changes + bleibt in Historie

## 🆘 Support

- [📖 Vollständige Dokumentation](https://github.com/your-username/ha-release-notes-manager#readme)
- [🐛 Issue Tracker](https://github.com/your-username/ha-release-notes-manager/issues)
- [💬 Discussions](https://github.com/your-username/ha-release-notes-manager/discussions)

## ⭐ Features im Detail

### Was macht diese Integration besonders?

**Automatisches Fehler-Management:**
Offene Fehler werden automatisch in neue Releases übernommen. Du musst sie nicht manuell kopieren. Sobald ein Fehler gelöst ist, erscheint er automatisch in den Änderungen und wird nicht mehr in neue Releases übernommen.

**Professionelle Darstellung:**
Mit kategorisierten Einträgen und farbcodierten Badges sehen deine Release Notes professionell aus. Perfekt für Dokumentation oder zum Teilen mit anderen.

**Einfache Bedienung:**
Intuitive Benutzeroberfläche mit Inline-Bearbeitung. Kein Umweg über YAML-Dateien oder komplizierte Konfigurationen.

**100% Offline:**
Funktioniert komplett ohne Internetverbindung. Keine externen Dependencies, keine CDNs. Alles läuft lokal in deinem Home Assistant.

---

**Entwickelt mit ❤️ für die Home Assistant Community**
