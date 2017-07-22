/**
 * \file
 * \brief List network card and collect information
 *
 * Copyright 2017 Uilian Ries <uilianries@gmail.com>
 */
#include <gtest/gtest.h>

#include <cpprest/version.h>

TEST(CppRestSDKTest, Version) {
  EXPECT_EQ(9, CPPREST_VERSION_MINOR);
  EXPECT_EQ(2, CPPREST_VERSION_MAJOR);
  EXPECT_EQ(0, CPPREST_VERSION_REVISION);
}
