set(TARGET_NAME cpp_application)

cmake_minimum_required(VERSION 3.15)

# Build
file(GLOB_RECURSE CURRENT_SRCS ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)

add_executable(${TARGET_NAME}
  main.cpp
  ${CURRENT_SRCS}
)

target_link_libraries(${TARGET_NAME}
)

target_include_directories(${TARGET_NAME}
  PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)

set(INSTALL_NAME_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../bin)
install(TARGETS ${TARGET_NAME} DESTINATION ${INSTALL_NAME_DIR})
