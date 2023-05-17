message(STATUS "CMake version: ${CMAKE_VERSION}")
cmake_minimum_required(VERSION 3.15)

set(PROJECT BasicCppProjectTemplate)
project(${PROJECT}
  LANGUAGES CXX
  VERSION "1.0.0"
)

set(CMAKE_VERBOSE_MAKEFILE OFF)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "Default build type to Debug" FORCE)
endif()

message("System:        ${CMAKE_SYSTEM_NAME}")
message("C compiller:   ${CMAKE_C_COMPILER}")
message("CXX compiller: ${CMAKE_CXX_COMPILER}")
message("Build type:    ${CMAKE_BUILD_TYPE}")

set(CXX_FLAGS "${APP_DEFS} -std=c++17" )
set(CXX_FLAGS "${CXX_FLAGS} " )

set(C_FLAGS "${APP_DEFS} -std=c99")
set(C_FLAGS "${C_FLAGS} -fdata-sections -ffunction-sections")
set(WARN_FLAGS "-Wall -Wextra -pedantic -Wconversion -Wsign-conversion -Winit-self -Wunreachable-code")

set(FLAGS_RELEASE "-O2")
set(FLAGS_DEBUG   "-O0 -g")

set(CMAKE_C_FLAGS_RELEASE    "${C_FLAGS} ${FLAGS_RELEASE} ${WARN_FLAGS}")
set(CMAKE_C_FLAGS_DEBUG      "${C_FLAGS} ${FLAGS_DEBUG} ${WARN_FLAGS}")
set(CMAKE_CXX_FLAGS_RELEASE  "${CXX_FLAGS} ${FLAGS_RELEASE} ${WARN_FLAGS}")
set(CMAKE_CXX_FLAGS_DEBUG    "${CXX_FLAGS} ${FLAGS_DEBUG} ${WARN_FLAGS}")

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED on)

add_subdirectory(src)

if(ENABLE_TESTS)
  enable_testing()
  find_package(gtest REQUIRED)
  add_subdirectory(test)
endif()
