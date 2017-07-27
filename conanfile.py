"""Conan.io recipe for CppRestSDK library
"""
from conans import ConanFile, CMake
from conans.model.options import OptionsValues
from conans.model.requires import Requirements
from os import path
from tempfile import mkdtemp


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
    requires = "Boost/1.60.0@lasote/stable", "OpenSSL/1.0.2l@conan/stable"
    cpprestsdk_dir = "%s-%s" % (name, version)
    install_dir = mkdtemp()
    default_options = "shared=True", \
        "Boost:without_container=True", \
        "Boost:without_context=True", \
        "Boost:without_coroutine=True", \
        "Boost:without_coroutine2=True", \
        "Boost:without_exception=True", \
        "Boost:without_graph=True", \
        "Boost:without_graph_parallel=True", \
        "Boost:without_iostreams=True", \
        "Boost:without_locale=True", \
        "Boost:without_log=True", \
        "Boost:without_math=True", \
        "Boost:without_mpi=True", \
        "Boost:without_program_options=True", \
        "Boost:without_serialization=True", \
        "Boost:without_signals=True", \
        "Boost:without_test=True", \
        "Boost:without_timer=True", \
        "Boost:without_type_erasure=True", \
        "Boost:without_wave=True"

    def source(self):
        self.run("git clone --depth=50 --branch=v%s %s.git %s" % (self.version, self.url, self.cpprestsdk_dir))

    def config_options(self):
        if self.settings.os == "Linux":
            self.options.values = OptionsValues.loads("Boost:fPIC=True")
        if self.settings.os == "Macos":
            self.options.remove("shared")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = self.install_dir
        cmake.definitions["BUILD_TESTS"] = True if self.scope.dev and self.scope.build_tests else False
        cmake.definitions["BUILD_SAMPLES"] = True if self.scope.dev and self.scope.build_samples else False
        if self.settings.os == "Macos":
            cmake.definitions["BUILD_SHARED_LIBS"] = True
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
