################################################################################
# CMake receipt for cpprestsdk test
#
# Copyright (c) Microsoft Corporation
################################################################################
PROJECT(conan-cpprestsdk-test)
cmake_minimum_required(VERSION 3.1.3)

# Import Conan package #########################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

# Build test ###################################################################
ADD_EXECUTABLE(${CMAKE_PROJECT_NAME} main.cpp)
TARGET_LINK_LIBRARIES(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})
SET_PROPERTY(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 11)


# Execute test #################################################################
ENABLE_TESTING()
ADD_TEST(http-request bin/${CMAKE_PROJECT_NAME})
