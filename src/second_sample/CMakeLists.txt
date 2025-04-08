
# Specify the source files
set(SOURCES main.cpp sample_class.cpp)

# Create an executable
add_executable(second_sample ${SOURCES})

# Specify the output directory for the binary
set_target_properties(second_sample PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/../bin
)