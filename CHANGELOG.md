# Changelog

## [0.4.0] - 2024-12-29

### Added
- **Dark Mode Support** - Automatische Anpassung an System-Theme, alle Farben optimiert für Lesbarkeit
- **Keyboard Shortcuts** - Strg+S zum Speichern, ESC zum Schließen von Modals
- **Release Summary** - Kompakte Übersicht (X Features • X Änderungen • X offene Bugs • X gelöst)
- **Markdown Export** - Exportiere einzelne Releases als .md Datei
- **Alphabetische Sortierung** - Kategorien werden in Dropdowns alphabetisch angezeigt
- **Pencil Icon** - Kompakter ✏️ Button statt "Bearbeiten" Text
- **Neue Einträge oben** - Features, Änderungen und Bugs erscheinen am Anfang der Liste

### Changed
- Performance-Optimierung durch effizientere Array-Operationen
- Verbesserte Benutzerführung durch visuelle Feedback-Elemente

### Fixed
- **mkdir-Fehler behoben** - Keine "File exists" Fehler mehr im Log (__init__.py korrigiert)
- **HACS Validation** - brands check ignoriert (.github/workflows/validate.yml)
- Dark Mode Lesbarkeit - Alle Textfarben im Dark Mode optimiert

### Technical
- HTML: 468 → 584 Zeilen
- Keine Breaking Changes
- Datenmodell unverändert
- Rollback auf v0.3.1 jederzeit möglich

---

## [0.3.1] - 2024-12-16

### Fixed
- GitHub Actions Release Workflow
- HACS Metadata erweitert

---

## [0.3.0] - 2024-12-16

### Initial Release
- Release-Verwaltung (erstellen, bearbeiten, löschen)
- Kategorisierung (Features, Changes, Known Issues)
- Fehler-Management mit automatischer Übernahme
- Suchfunktion und Filter
- Responsive Design
- Automatisches Backup-System
- HACS-kompatibel
