import glob
import os.path

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"

# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

import os
print("IN INSTALLATION SCRIPT")
print("pwd: ", os.getcwd())
print("ls ..:", os.listdir(os.path.dirname(os.getcwd())))
print("END OF INSTALLATION SCRIPT")

# Handle improperly checked-out symlinks from git.
# This happens for certain Windows users depending on git config
if not os.path.isdir("src/cpp-core"):
    import shutil
    os.remove("src/cpp-core")
    shutil.copytree("../r/src/cpp-core", "src/cpp-core")


ext_modules = [
    Pybind11Extension("polyglotpackaging.cpp",
        sorted(
            ["src/main.cpp"] +
            glob.glob("src/cpp-core/*.cpp"),
        ),
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        extra_compile_args = ['-std=c++17']
        ),
]

setup(
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    version = __version__
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
)

