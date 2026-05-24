#========================================================================== */
#                                   TESTS                                   */
#========================================================================== */
include(GoogleTest)

message("-- Add tests")
add_executable(test_hello test_hello.cpp)
target_link_libraries(test_hello PRIVATE demo_lib GTest::gtest_main)

add_test(NAME hello_test COMMAND test_hello)


gtest_discover_tests(test_hello)
