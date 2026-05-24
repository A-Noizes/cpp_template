# ========================================================================== #
#                                   COMPILER                                 #
# ========================================================================== #
set(COMPILER_SETTINGS_USER "")

# =========================================================
# Warnings / Strict Compiler Diagnostics
# =========================================================

if(WARNINGS_SETTING)

    list(APPEND COMPILER_SETTINGS_USER

        # Base warnings
        "-Wall"
        "-Wextra"
        "-Wpedantic"

        # Important strict warnings
        "-Wshadow"
        "-Wconversion"
        "-Wsign-conversion"

        # Additional useful diagnostics
        "-Wformat=2"
        "-Wundef"
        "-Wnull-dereference"
        "-Wcast-align"

        # Better stack traces / sanitizer support
        "-fno-omit-frame-pointer"
    )

    # GCC specific warnings
    if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")

        list(APPEND COMPILER_SETTINGS_USER
            "-Walloc-zero"
            "-Wduplicated-cond"
            "-Wduplicated-branches"
            "-Wlogical-op"
            "-Wrestrict"
        )

    endif()

endif()


# =========================================================
# Sanitizers
# =========================================================

if(SANITISER_SETTINGS)

    list(APPEND COMPILER_SETTINGS_USER
        "-fsanitize=address"
        "-fsanitize=undefined"
    )

endif()


# =========================================================
# Debug Settings
# =========================================================

if(COMPILER_DEBUG_SETTINGS)

    list(APPEND COMPILER_SETTINGS_USER
        "-DDEBUG"
    )

    # Only for GCC/libstdc++
    if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")

        list(APPEND COMPILER_SETTINGS_USER
            "-D_GLIBCXX_DEBUG"
        )

    endif()

endif()


# =========================================================
# Debug Optimisation + Symbols
# =========================================================

if(COMPILER_OPTIMISATION_SETTINGS)

    list(APPEND COMPILER_SETTINGS_USER
        "-Og"
        "-g3"
    )

endif()


# Add Release-specific optimisation flags when building Release
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    list(APPEND COMPILER_SETTINGS_USER
        "-O3"
        "-DNDEBUG"
    )
endif()


# =========================================================
# Output compiler info
# =========================================================

message(STATUS "Compiler: ${CMAKE_CXX_COMPILER_ID}")


# =========================================================
# Compile options
# =========================================================

add_compile_options(${COMPILER_SETTINGS_USER})


# =========================================================
# Linker flags for sanitizers
# =========================================================

if(SANITISER_SETTINGS)

    add_link_options(
        "-fsanitize=address"
        "-fsanitize=undefined"
    )

endif()