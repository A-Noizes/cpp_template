#!/usr/bin/env python3

import toml
import re
import pathlib as pl
import sys
import datetime as dt


class _Color:
    RESET = "\x1b[0m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"


def _supports_color() -> bool:
    return sys.stdout.isatty()


def _c(text: str, color_code: str) -> str:
    if _supports_color():
        return f"{color_code}{text}{_Color.RESET}"
    return text



PIXI_TOML           = pl.Path(__file__).resolve().parents[1] / "pixi.toml"
cmake         = pl.Path(__file__).resolve().parents[1] / "cmake"
FIND_PACKAGES_CMAKE = pl.Path(__file__).resolve().parents[1] / "cmake" / "find_packages.cmake"


if not PIXI_TOML.exists():
    raise FileExistsError(f"Could not find ${PIXI_TOML}")
 
# Run metadata and banners
_START_TIME = dt.datetime.now()
print(_c("========================================", _Color.RESET))
print(_c(f"Dependency helper started: {_START_TIME.isoformat(sep=' ', timespec='seconds')}", _Color.RESET))
print(_c("Scanning dependencies and preparing CMake fragments...", _Color.RESET))
print(_c("========================================", _Color.RESET))

# Counters for summary
_created_count = 0
_existing_count = 0

dependencies: dict = toml.loads(PIXI_TOML.read_text())
for dependencie in dependencies["dependencies"].keys():
 
    
    version = re.sub(rf"[=><]{0,2}", "",dependencies["dependencies"][dependencie])
    

    find_statement  = f"find_package(${dependencie} {version} REQUIRED)"
    dependency_content = FIND_PACKAGES_CMAKE.read_text()
    if dependencie  not in dependency_content:
        print(_c(f"[WARN] New dependency '{dependencie}' detected. Update {FIND_PACKAGES_CMAKE.name}", _Color.YELLOW))
        FIND_PACKAGES_CMAKE.write_text(dependency_content + "\n" + find_statement)
    else:
        _existing_count += 1
        print(_c(f"[INFO] '{dependencie}' already exists at {FIND_PACKAGES_CMAKE.name}", _Color.BLUE))
        continue
    
    
    
    _created_count += 1
    print(_c(f"[OK] Dependency '{dependencie}' successfully written to {FIND_PACKAGES_CMAKE.name}", _Color.GREEN))
    

# Summary
_END_TIME = dt.datetime.now()
_duration = _END_TIME - _START_TIME
print(_c("----------------------------------------", _Color.RESET))
print(_c(f"Summary: created {_created_count}, already existing {_existing_count}, total {len(dependencies)}", _Color.RESET))
print(_c(f"Finished: {_END_TIME.isoformat(sep=' ', timespec='seconds')} (duration: {_duration})", _Color.RESET))
print(_c("========================================", _Color.RESET))

