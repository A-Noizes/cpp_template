import json
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


preset     = sys.argv[1]
ROOT       = pl.Path(__file__).resolve().parents[1] 
RESET_JSON = ROOT / "CMakePresets.json"
PRESETS    = json.loads(RESET_JSON.read_text())

_created = 0
_updated = 0



_START_TIME = dt.datetime.now()
print(_c("========================================", _Color.RESET))
print(_c(f"LSP helper started: {_START_TIME.isoformat(sep=' ', timespec='seconds')}", _Color.RESET))
print(_c(f"Using preset: {preset}", _Color.RESET))
print(_c("========================================", _Color.RESET))

target_configure = [ configure for configure in PRESETS["configurePresets"]  if configure["name"] == preset ]
if not target_configure:
    raise RuntimeError(_c(f"CMake Preset '{preset}' not found in {RESET_JSON}", _Color.RED))

binary_path = str(target_configure[0]["binaryDir"])\
                            .replace("${presetName}", preset)\
                            .replace("${sourceDir}/", "")



clangd_setting = ROOT / ".clangd"
if not clangd_setting.exists():
    print(_c(f"Create `.clangd` config file", _Color.BLUE))
    clangd_setting.touch()
    clangd_database = (ROOT / "assets" /"templates" / "clangd" / "clangd.jinja")\
                        .read_text() \
                        .replace("{{build}}", str(binary_path))
    clangd_setting.write_text(clangd_database)
else:
    print(_c(f"`.clangd` config file allready exists", _Color.BLUE))
    
    
    

# Summary
_END_TIME = dt.datetime.now()
_duration = _END_TIME - _START_TIME
print(_c("----------------------------------------", _Color.RESET))
print(_c(f"Summary: created {_created}, updated {_updated}", _Color.RESET))
print(_c(f"Finished: {_END_TIME.isoformat(sep=' ', timespec='seconds')} (duration: {_duration})", _Color.RESET))
print(_c("========================================", _Color.RESET))