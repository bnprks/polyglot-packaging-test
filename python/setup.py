import glob

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
import importlib.metadata


__version__ = importlib.metadata.version(__package__)

# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

import os
print("IN INSTALLATION SCRIPT")
print("pwd: ", os.getcwd())
print("ls ..:", os.listdir(os.path.dirname(os.getcwd())))
print("END OF INSTALLATION SCRIPT")
# raise Exception("GLOB GLOB GLOB GLOB GLOB:" + str(glob.glob("src/cpp-core/*.cpp")))

ext_modules = [
    Pybind11Extension("polyglotpackaging.cpp",
        sorted(
            ["src/main.cpp"] +
            glob.glob("src/cpp-core/*.cpp"),
        ),
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        cxx_standard=17,
        ),
]

setup(
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
)

