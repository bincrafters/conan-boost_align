#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostAlignConan(base.BoostBaseConan):
    name = "boost_align"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_align"
    lib_short_names = ["align"]
    header_only_libs = ["align"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_static_assert",
        "boost_throw_exception"
    ]
