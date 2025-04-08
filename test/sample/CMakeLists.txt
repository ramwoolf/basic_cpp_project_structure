cmake_minimum_required(VERSION 3.10)

set(TEST_TARGET_NAME test_sample)

# Find Google Test
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# Specify the test source files
set(TEST_SOURCES test_main.cpp)

set(SUT_SOURCES
    ${CMAKE_SOURCE_DIR}/src/sample/sample.cpp
)

# Create a test executable
add_executable(${TEST_TARGET_NAME} ${TEST_SOURCES} ${SUT_SOURCES})

# Link the test executable against Google Test and the project1 executable
target_link_libraries(${TEST_TARGET_NAME} 
    PRIVATE ${GTEST_LIBRARIES} 
)

target_include_directories(${TEST_TARGET_NAME} 
    PRIVATE ${CMAKE_SOURCE_DIR}/src
)

# Add a test
add_test(NAME TestSample COMMAND ${TEST_TARGET_NAME})