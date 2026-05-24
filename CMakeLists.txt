#========================================================================== */
#                                MAIN CMAKE                                 */
#========================================================================== */

cmake_minimum_required(VERSION 3.17.0)
project(vs_cpp_setup VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS OFF)


#================================================================
# Cmake includes
#================================================================
include("${CMAKE_SOURCE_DIR}/cmake/toml_parser.cmake")
include("${CMAKE_SOURCE_DIR}/cmake/options.cmake")
include("${CMAKE_SOURCE_DIR}/cmake/compiler.cmake")
include("${CMAKE_SOURCE_DIR}/cmake/find_packages.cmake")
include("${CMAKE_SOURCE_DIR}/cmake/dependencies.cmake")
include("${CMAKE_SOURCE_DIR}/cmake/subdirectories.cmake")
include("${CMAKE_SOURCE_DIR}/cmake/unit_tests.cmake")




#================================================================
# Main
#================================================================
add_executable(${PROJECT_NAME} "${CMAKE_SOURCE_DIR}/src/main.cpp")
target_link_libraries(
    ${PROJECT_NAME} 
    PRIVATE 
    demo_lib
    GTest::gtest_main 
    fmt::fmt
)


# Install rules
install(TARGETS ${PROJECT_NAME} demo_lib
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Install public headers
install(DIRECTORY ${CMAKE_SOURCE_DIR}/src/demo_lib/include/ DESTINATION include)



#================================================================
# Testing
#================================================================
enable_testing()





