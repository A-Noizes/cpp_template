# Makefile — Hilfs-Targets zum schnellen Bauen, Testen und pixi-Befehlen
# Nutzung: `make help` für Übersicht. Standard-Preset: `debug`.

PRESET ?= debug
BUILD_DIR := out/build/$(PRESET)
CMAKE := cmake
CTEST := ctest
PIXICMD := pixi

.PHONY: help configure build debug release all test run pixi-init pixi-install clean

help:
	@echo "Makefile — verfügbare Targets:"
	@echo "  help           - Diese Hilfe anzeigen"
	@echo "  configure      - CMake konfigurieren (Preset: $(PRESET))"
	@echo "  build          - Build ausführen (führt configure aus)"
	@echo "  release        - Build mit Preset=release"
	@echo "  test           - Tests mit ctest ausführen (benötigt Build)"
	@echo "  run            - Beispiel-Executable aus dem Build-Ordner starten"
	@echo "  pixi-init      - 'pixi init' im Projektverzeichnis ausführen"
	@echo "  pixi-install   - 'pixi install' ausführen"
	@echo "  clean          - Build-Ordner entfernen"

configure:
	@echo "Configuring (preset=$(PRESET))..."
	$(CMAKE) --preset $(PRESET)

build: configure
	@echo "Building (preset=$(PRESET))..."
	$(CMAKE) --build --preset $(PRESET)

release:
	@echo "Building release preset..."
	$(MAKE) PRESET=release build

debug:
	@echo "Building debug preset..."
	$(MAKE) PRESET=debug build

test: build
	@echo "Running tests (test-dir=$(BUILD_DIR))..."
	$(CTEST) --test-dir $(BUILD_DIR) -V

run: build
	@echo "Running executable from $(BUILD_DIR)..."
	$(BUILD_DIR)/vs_cpp_setup || true

pixi-init:
	@echo "Running: $(PIXICMD) init"
	$(PIXICMD) init

pixi-install:
	@echo "Running: $(PIXICMD) install"
	$(PIXICMD) install

clean:
	@echo "Removing build output..."
	@rm -rf out/build/*

all: build test
