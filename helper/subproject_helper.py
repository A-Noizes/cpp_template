
import sys
import pathlib as pl
import re
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


TEMPLATE_DIR      = pl.Path(__file__).resolve().parents[1] / "assets" / "templates" / "library"
TEMPLATE_DIR_TEST = pl.Path(__file__).resolve().parents[1] / "assets" / "templates" / "test"
LIB_DIR           = pl.Path(__file__).resolve().parents[1] / "src"
TEST_DIR          = pl.Path(__file__).resolve().parents[1] / "test"
cmake       = pl.Path(__file__).resolve().parents[1] / "cmake"

lib_name  = sys.argv[1]
lib_root  = LIB_DIR / lib_name
lib_src   = lib_root / "src"
lib_inc   = lib_root / "include"
test_root = TEST_DIR / lib_name

# Start banner
_START_TIME = dt.datetime.now()
print(_c("========================================", _Color.RESET))
print(_c(f"Subproject helper started: {_START_TIME.isoformat(sep=' ', timespec='seconds')}", _Color.RESET))
print(_c(f"Preparing subproject '{lib_name}' in {LIB_DIR}", _Color.RESET))
print(_c("========================================", _Color.RESET))

# Counters
_created_count = 0
_skipped_count = 0

for dir in [lib_root, lib_src, lib_inc]:
    if not dir.exists():
        print(_c(f"[WARN] Creating directory: {dir}", _Color.YELLOW))
        dir.mkdir(parents=True)
        _created_count += 1
    else:
        print(_c(f"[INFO] Directory exists: {dir}", _Color.BLUE))
        _skipped_count += 1

templates = list(TEMPLATE_DIR.glob("**/*.jinja"))
if not templates:
    raise FileExistsError(_c(f"Template files missing in {TEMPLATE_DIR}", _Color.RED))


for template in templates:
    file_name = template.stem
    content   = template.read_text() \
                        .replace("{{name}}", lib_name)

    if ".h" in file_name:
        target = lib_inc / f"{lib_name}.h"
        target.write_text(content)
        _created_count += 1
        print(_c(f"[OK] Wrote header {target}", _Color.GREEN))

    if ".cpp" in file_name:
        target = lib_src / f"{lib_name}.cpp"
        target.write_text(content)
        _created_count += 1
        print(_c(f"[OK] Wrote source {target}", _Color.GREEN))

    if "CMake" in file_name:
        target = lib_root / file_name
        target.write_text(content)
        _created_count += 1
        print(_c(f"[OK] Wrote CMake fragment {target}", _Color.GREEN))
   
   


test_on = bool(sys.argv[2])
if test_on:
    if not test_root.exists():
        print(_c(f"[WARN] Creating test directory: {dir}", _Color.YELLOW))
        test_root.mkdir()
        cmake_test_template = TEMPLATE_DIR_TEST / "CMakeLists.txt.jinja"
        content             = cmake_test_template.read_text() \
                                                .replace("{{lib}}", lib_name) \
                                                .replace("{{command}}", f"test_{lib_name}") \
                                                .replace("{{test_name}}", f"{lib_name}_gtest")   
        target = test_root / cmake_test_template.stem
        target.write_text(content)
        
        print(_c(f"[OK] Wrote test {target}", _Color.GREEN))
        
        cpp_test_template = TEMPLATE_DIR_TEST / "test.cpp.jinja"
        content  = cpp_test_template.read_text() \
                                    .replace("{{lib}}", lib_name) \
                                    .replace("{{test_name}}", f"Test{lib_name}")
        
        target = test_root / f"test_{lib_name}.cpp"
        target.write_text(content)
        
        
        print(_c(f"[OK] Wrote {target}", _Color.GREEN))
        _created_count += 1
    else:
        print(_c(f"[INFO] Test directory exists: {test_root}", _Color.BLUE))
        _skipped_count += 1
        
        
else:
    print(_c(f"[INFO] Skip test directory building", _Color.BLUE))
    _skipped_count += 1
    
        
#Update subdirectories.cmake
subdirectory_declaration = "add_subdirectory(${CMAKE_SOURCE_DIR}/src/" + lib_name + ")\n"
subdirectory_test        = "add_subdirectory(${CMAKE_SOURCE_DIR}/test/" + lib_name + ")\n"
cmake_files_subdirectory = {"subdirectories.cmake" : subdirectory_declaration, "unit_tests.cmake" : subdirectory_test}
for dir in cmake_files_subdirectory.keys():
    cmake_sub                = cmake / dir
    cmake_content            = cmake_sub.read_text()
    declaration              = cmake_files_subdirectory[dir]
    if declaration not in cmake_content:
        cmake_sub.write_text(cmake_content + declaration)
        print(_c(f"[OK] {cmake_sub.name} updated", _Color.GREEN))
    

    
# Summary
_END_TIME = dt.datetime.now()
_duration = _END_TIME - _START_TIME
print(_c("----------------------------------------", _Color.RESET))
print(_c(f"Summary: created {_created_count}, skipped {_skipped_count}", _Color.RESET))
print(_c(f"Finished: {_END_TIME.isoformat(sep=' ', timespec='seconds')} (duration: {_duration})", _Color.RESET))
print(_c("========================================", _Color.RESET))
        