cmake_minimum_required(VERSION 4.0)

project(SmallProjects)

# Add subdirectories for each project
add_subdirectory(src/sample)
add_subdirectory(src/second_sample)

# Add subdirectories for tests
enable_testing()
add_subdirectory(test/sample)
