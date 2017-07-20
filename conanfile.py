"""Conan.io recipe for CppRestSDK library
"""
from conans import ConanFile, CMake, tools
from os import path

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
    default_options = "shared=True", "Boost:fPIC=True"
    cpprestsdk_dir = "%s-%s" % (name, version)

    def source(self):
        self.run("git clone --depth=50 --branch=v%s %s.git %s" % (self.version, self.url, self.cpprestsdk_dir))

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTS"] = True if self.scope.dev and self.scope.build_tests else False
        cmake.definitions["BUILD_SAMPLES"] = True if self.scope.dev and self.scope.build_samples else False
        if cmake.definitions["BUILD_TESTS"] and self.settings.os == "Linux":
            self._insert_pthread()
        cmake.configure()
        cmake.build()

    def _insert_pthread(self):
        # test_runner does not find pthread_create
        old_line = "        -Wl,--whole-archive"
        new_line = """        -Wl,--whole-archive
        pthread"""
        cmake_path = path.join(self.cpprestsdk_dir, "Release", "tests", "common", "TestRunner", "CMakeLists.txt")
        tools.replace_in_file(cmake_path, old_line, new_line)


    def package(self):
        release_dir = path.join(self.cpprestsdk_dir, "Release")
        self.copy("license.txt",  dst=".", src=self.cpprestsdk_dir)
        self.copy(pattern="*.h", dst="include", src=path.join(release_dir, "include"))
        self.copy(pattern="*.hpp", dst="include", src=path.join(release_dir, "include"))
        self.copy(pattern="*.dat", dst="include", src=path.join(release_dir, "include"))
        self.copy(pattern="*.so*", dst="lib", src=path.join(release_dir, "Binaries"), keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs.append("cpprest")
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
