"""This script build Conan.io package to multiple platforms."""
from conan.packager import ConanMultiPackager
from copy import copy


if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing")
    builder.add_common_builds(shared_option_name="cpprestsdk:shared", pure_c=False)
    # For Linux + Clang use libc++
    if settings["compiler"] == "clang" and settings["os"] == "Linux":
        clang_builds = []
        for settings, options, env_vars, build_requires in builder.builds:
            settings["libcxx"] = "libc++"
            clang_builds.append([settings, options, env_vars, build_requires])
        builder.builds = clang_builds
    builder.run()
