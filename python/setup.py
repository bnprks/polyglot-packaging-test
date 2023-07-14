import glob
import os.path

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup
from setuptools.command.install import install

__version__ = "0.0.1"

# Handle improperly checked-out symlinks from git by manual copying
# This happens for certain Windows users depending on git config
if not os.path.islink("src/cpp-core") and not os.path.isdir("src/cpp-core"):
    import shutil
    contents = open("src/cpp-core", "rb").read()
    os.remove("src/cpp-core")
    shutil.copytree("../r/src/cpp-core", "src/cpp-core")
    open("src/cpp-core/old-cpp-core", "wb").write(contents)

class PostInstallHook(install):
    def run(self):
        install.run(self)
        # Undo the manual copying of symlinks
        if not os.path.islink("src/cpp-core") and os.path.isfile("src/cpp-core/old-cpp-core"):
            import shutil
            contents = open("src/cpp-core/old-cpp-core", "rb").read()
            shutil.rmtree("src/cpp-core")
            open("src/cpp-core", "wb").write(contents)


ext_modules = [
    Pybind11Extension("polyglotpackaging.cpp",
        # Sort input files to ensure reproducible builds (https://github.com/pybind/python_example/pull/53)
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
    cmdclass={"install":PostInstallHook},
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    version = __version__
)

