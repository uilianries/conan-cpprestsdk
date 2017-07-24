"""Conan.io recipe for CppRestSDK library
"""
from conans import ConanFile, CMake, tools
from os import path
from tempfile import mkdtemp
import subprocess


class CppRestSDKConan(ConanFile):
    """Checkout CppRestSDK, build and create package
    """
    name = "cpprestsdk"
    version = "2.9.1"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    exports_sources = "CMakeLists.txt"
    url = "https://github.com/Microsoft/cpprestsdk"
    author = "Uilian Ries <uilianries@gmail.com>"
    description = "A project for cloud-based client-server communication in native code using a modern asynchronous C++ API design"
    license = "https://github.com/Microsoft/cpprestsdk/blob/master/license.txt"
    requires = "Boost/1.62.0@lasote/stable", "OpenSSL/1.0.2l@conan/stable"
    default_options = "shared=True"
    cpprestsdk_dir = "%s-%s" % (name, version)
    install_dir = mkdtemp()

    def source(self):
        self.run("git clone --depth=50 --branch=v%s %s.git %s" % (self.version, self.url, self.cpprestsdk_dir))

    def config_options(self):
        if self.settings.os == "Linux":
            self.default_options = self.default_options, "Boost:fPIC=True"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = self.install_dir
        cmake.definitions["BUILD_TESTS"] = True if self.scope.dev and self.scope.build_tests else False
        cmake.definitions["BUILD_SAMPLES"] = True if self.scope.dev and self.scope.build_samples else False
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("license.txt",  dst=".", src=self.cpprestsdk_dir)
        self.copy(pattern="*", dst="include", src=path.join(self.install_dir, "include"))
        self.copy(pattern="*", dst="lib", src=path.join(self.install_dir, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs.append("cpprest")
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
