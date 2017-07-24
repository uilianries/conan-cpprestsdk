"""This script build Conan.io package to multiple platforms."""
from conan.packager import ConanMultiPackager
from copy import copy
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing")
    builder.add_common_builds(shared_option_name="cpprestsdk:shared", pure_c=False)
    # For Linux + Clang use libc++
    filtered_builds = []
    for settings, options, env_vars, build_requires in builder.builds:
        print(settings)
        if settings["compiler"] == "clang" and platform.system() == "Linux":
                settings["compiler.libcxx"] = "libc++"
        filtered_builds.append([settings, options, env_vars, build_requires])
    builder.builds = filtered_builds
    builder.run()
