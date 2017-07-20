PROJECT(conan-cpprestsdk)

MESSAGE("Conan CppRestSDK Wrapped CMake")
cmake_minimum_required(VERSION 2.8.12)
include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

add_subdirectory("cpprestsdk-2.9.1/Release")
