cmake_minimum_required(VERSION 3.14)
project(PolyglotPackaging)


### BUILD SETUP ###

set(CMAKE_CXX_STANDARD 17)

set(SRC cpp-core)

add_library(
    polyglot
    ${SRC}/add.cpp
    ${SRC}/message.cpp
)

target_include_directories(
    polyglot
    PUBLIC
    ${SRC}
)

### TESTING ###
enable_testing()

# For newer cmake, suprress a cmake warning
if(POLICY CMP0135)
    cmake_policy(SET CMP0135 NEW)
endif()
include(FetchContent)
FetchContent_Declare(googletest URL https://github.com/google/googletest/archive/c88e0b4673f9b08818e0e74c4ed718db5f9b809c.zip)

FetchContent_MakeAvailable(googletest)
include(GoogleTest)



add_executable(test_basic tests/test_basic.cpp)
target_link_libraries(test_basic polyglot gtest_main)
gtest_discover_tests(test_basic)
