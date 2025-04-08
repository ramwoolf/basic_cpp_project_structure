#include <gtest/gtest.h>

#include "sample/sample.hpp"
// #include "../src/sample/sample.hpp"

// Example test case
TEST(SampleTest, CallSample) {
    EXPECT_EQ(get_square(2), 4);
}

TEST(SampleTest, CallSample2) {
    EXPECT_EQ(get_square(3), 9);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}