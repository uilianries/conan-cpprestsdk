/**
 * \file
 * \brief List network card and collect information
 *
 * Copyright 2017 Uilian Ries <uilianries@gmail.com>
 */
#define CATCH_CONFIG_MAIN
#include <catch.hpp>

#include <cpprest/version.h>

TEST_CASE( "CppRestSDK Version", "[version]" ) {
    REQUIRE( CPPREST_VERSION_MINOR == 9 );
    REQUIRE( CPPREST_VERSION_MAJOR == 2 );
    REQUIRE( CPPREST_VERSION_REVISION == 0 );
}
