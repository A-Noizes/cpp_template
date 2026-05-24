# vs_cpp_setup — C++ Projekt mit CMake

Dieses Repository enthält ein Beispielprojekt mit CMake-, Hilfs- und Template-Dateien, einer kleinen Beispielanwendung und Unit-Tests (GoogleTest). Ziel ist ein reproduzierbares, leicht erweiterbares C++-Projekt-Setup, das als Vorlage für neue Bibliotheken/Subprojekte dient.

## Inhalt / Struktur

- `CMakeLists.txt`, `cmake/`: Haupt-CMake-Konfiguration und Hilfs-Skripte.
- `src/`: Beispielanwendung und Quellcode (`main.cpp`, `hello/`).
- `tests/`: Beispiel-Unit-Tests (GoogleTest).
- `assets/templates/`: Jinja-Templates zum Erzeugen neuer Bibliotheken/Projekte.
- `helper/`: Python-Hilfs-Skripte für Abhängigkeiten und LSP-Integration.
- `Dependencies.json`, `cmake/dependencies.cmake`: deklarative Abhängigkeiten + Helpers (CPM).

## Abhängigkeiten

Dieses Projekt verwendet CMake-Presets und CPM für externe Abhängigkeiten. Stelle sicher, dass auf deinem System mindestens CMake (>=3.19), ein C++-Compiler und Python 3 verfügbar sind.

## Bauen

Es sind CMake-Presets vorhanden (siehe `CMakePresets.json`). Beispiel (Debug):

```bash
cmake --preset debug
cmake --build --preset debug
```

Für Release-Builds ersetze `debug` durch das passende Preset (z. B. `release`). Der Build-Output landet im Preset-konfigurierten Ordner (üblich: `out/build/<preset>`).

Nach dem Build findest du ausführbare Targets im Build-Output; die Namen der Targets stehen in den jeweiligen `CMakeLists.txt`-Dateien.

## Tests

Unit-Tests befinden sich in `tests/` und verwenden GoogleTest. Nach dem Build kannst du die Tests mit `ctest` ausführen (Debug-Beispiel):

```bash
ctest --test-dir out/build/debug -V
```

Wenn du ein anderes Preset benutzt, passe den Pfad entsprechend an.

## Neue Bibliothek / Subprojekt anlegen

Es gibt Vorlagen unter `assets/templates/` (inkl. `library`-Template). Verwende die Templates zusammen mit `helper/subproject_helper.py` oder kopiere die Struktur manuell, um neue Subprojekte zu erzeugen.

## Entwicklung & LSP

Die Datei `helper/lsp_helper.py` enthält Hilfen zur Integration mit LSP/clangd; `assets/templates/clangd/clangd.jinja` ist eine Vorlage für clangd-Konfigurationen.

## Beiträge

- Fork, Branch, Commit und öffne einen Pull Request.
- Bitte Tests lokal ausführen und sicherstellen, dass der Build grün ist.

## Weiteres

Wenn du möchtest, kann ich die README noch um Beispiele für typische CMake-Targets, ein kurzes Setup-Skript oder eine Schritt-für-Schritt-Anleitung zum Erstellen eines neuen Subprojekts ergänzen.

---
Diese README ersetzt die ursprüngliche Kurz-Anleitung für die Tests und dokumentiert das gesamte Projekt.
