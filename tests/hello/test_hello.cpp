#include <gtest/gtest.h>
#include "demo_lib.h"

TEST(HelloTest, PrintHelloDoesNotThrow) {
    EXPECT_NO_THROW(hello());
}



int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
