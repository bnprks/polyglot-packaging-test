import sys
# See https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

try:
    __version__ = metadata.version("polyglot-packaging")
except:
    __version__ = '0.dev0+unknown'