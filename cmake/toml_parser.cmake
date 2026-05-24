
#========================================================================== */
#                                TOML PARSER                                */
#========================================================================== */

message("=================================================================")
message("PROJECT DESCRIPTION")
file(STRINGS "${CMAKE_SOURCE_DIR}/pixi.toml" toml)
foreach(line in ${toml})

    if("${line}" MATCHES "author" )
        string(REPLACE "="  ":" author "${line}")
        string(REGEX REPLACE "\\[|\\]" "" author "${author}")
        message("-- ${author}")
    endif()

    if("${line}" MATCHES "name")
        string(REPLACE "="  ":" name_project "${line}")
        message("-- ${name_project}")
    endif()

    if("${line}" MATCHES "version")
        string(REPLACE "="  ":" version "${line}")
        message("-- ${version}")
    endif()

    if("${line}" MATCHES "channels")
        string(REPLACE "="  ":" channels "${line}")
        string(REGEX REPLACE "\\[|\\]" "" channels "${channels}")
        message("-- ${channels}")
    endif()

    if("${line}" MATCHES "platforms")
        string(REPLACE "="  ":" platforms "${line}")
        string(REGEX REPLACE "\\[|\\]" "" platforms "${platforms}")
        message("-- ${platforms}")
    endif()

endforeach()
