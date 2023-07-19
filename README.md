# Polyglot packaging test

This is a demo repository showcasing how to make a small C++ package
with bindings in both R and Python. The key feature is that the code
can be directly installed from the github source in both R and Python.

## Python installation
`pip install "git+https://github.com/bnprks/polyglot-packaging-test#subdirectory=python"`

## R installation
`remotes::install_github("bnprks/polyglot-packaging-test/r")`



## Development guide

Helper scripts included for building docs and running tests. Within `r`, `python`, or `cpp`
run `bash scripts/run_tests.sh` or `bash scripts/build_docs.sh`. Run from the root directory
to run tests/docs for all languages in one command.

## R

**Dev requirements**: `install.packages(c("pkgdown", "devtools", "testthat"))`
 - Documentation uses `pkgdown`
 - Tests use `testthat`

## Python

**Dev requirements**: [tox](https://tox.wiki/en/stable/installation.html)
 - Documentation uses `Sphinx` with [PyData theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/)
 - Tests use `pytest`
 - Includes a helper file with the overal project home page, linking to C++, R, and Python docs.
 - `tox` handles virtualenv setup for tests + documentation

## C++

**Dev requirements**: cmake, doxygen
 - Documentation uses Doxygen with the [Doxygen Awesome theme](https://jothepro.github.io/doxygen-awesome-css/index.html)
 - Tests use googletest + cmake + ctest

### VS Code editing extensions

- Python: autoDocstring
- C++: Doxygen Documentation Generator
