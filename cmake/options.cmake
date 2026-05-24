# ========================================================================== #
#                                   OPTIONS                                  #
# ========================================================================== #
option(WARNINGS_SETTING "Activate Compiler WARN Settings")
option(SANITISER_SETTINGS "Activate Compiler Sanitiser Settings")
option(COMPILER_DEBUG_SETTINGS "Activate Compiler DEBUG Settings")
option(COMPILER_OPTIMISATION_SETTINGS "Activate Compiler Optimisation Settings")


set(SETTINGS_LIST 
    ${WARNINGS_SETTING}
    ${SANITISER_SETTINGS}
    ${COMPILER_DEBUG_SETTINGS}
    ${COMPILER_OPTIMISATION_SETTINGS}
)

set(SETTINGS_FLAG
    "WARNINGS_SETTING"
    "SANITISER_SETTINGS"
    "COMPILER_DEBUG_SETTINGS"
    "COMPILER_OPTIMISATION_SETTINGS"
)

#=========================================================
#Print options                        
#=========================================================

message("=================================================================")
message("PROJECT SETTINGS")
foreach(flag setting IN ZIP_LISTS SETTINGS_FLAG SETTINGS_LIST)
    message("-- -D${flag}: ${setting}")
endforeach()


