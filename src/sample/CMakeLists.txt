
# Specify the source files
set(SOURCES main.cpp sample.cpp)

# Create an executable
add_executable(sample ${SOURCES})

# Specify the output directory for the binary
set_target_properties(sample PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/../bin
)