# Polyglot packaging test

This is a demo repository showcasing how to make a small C++ package
with bindings in both R and Python. The key feature is that the code
can be directly installed from the github source in both R and Python.

## Python installation
`pip install "git+https://github.com/bnprks/polyglot-packaging-test#subdirectory=python"`

## R installation
`remotes::install_github("bnprks/polyglot-packaging-test/r")`



## Documentation

### R
Uses `pkgdown` with a standard setup.

**Build + Deploy**:

- For testing, just do `pkgdown::build_site()`. Keeps an untracked copy in `r/docs`
- For deployment, do `pkgdown::deploy_to_branch(subdir="r/docs")`


### Python
Uses Sphinx with MyST to allow for markdown-format docs.

**Editing extensions**
VS Code autoDocstring
