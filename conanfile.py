from conans import ConanFile, tools, os

class BoostAlignConan(ConanFile):
    name = "Boost.Align"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/align"
    description = "For a description of this library, please visit http://boost.org/align "
    license = "www.boost.org/users/license.html"
    lib_short_name = "align"
    requires =  "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing"
    
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = src=os.path.join(os.getcwd(), self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)
