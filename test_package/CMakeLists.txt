################################################################################
# CMake receipt for cpprestsdk test
#
# Copyright (c) Microsoft Corporation
################################################################################
project(conan-cpprestsdk-test)
cmake_minimum_required(VERSION 3.1.3)

# Import Conan package #########################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Build test ###################################################################
add_executable(${CMAKE_PROJECT_NAME} main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 11)

# Execute test #################################################################
enable_testing()
add_test(http-request bin/${CMAKE_PROJECT_NAME})
