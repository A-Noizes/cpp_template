#========================================================================== */
#                                  LIBRARY                                  */
#========================================================================== */
message("-- Add library: demo_lib")
add_library(demo_lib )
target_sources(
    demo_lib
    PRIVATE
        "${CMAKE_CURRENT_SOURCE_DIR}/src/demo_lib.cpp"
    
    PUBLIC
    FILE_SET header_demo_lib
    TYPE HEADERS
    BASE_DIRS
      "${CMAKE_CURRENT_SOURCE_DIR}/include"
    FILES
      "include/demo_lib.h"
)
target_link_libraries(demo_lib PUBLIC fmt::fmt)

