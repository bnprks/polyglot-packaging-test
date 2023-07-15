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

**Build**:

- `pkgdown::build_site()` from within the `r` directory

### Python
Uses Sphinx with MyST to allow for markdown-format docs.

**Build**:

- `make html` from within the `python/docs` directory

**Editing extensions**:
- VS Code autoDocstring


### Github Pages
Github pages html files are present in the `gh-pages` branch. For local development and updating
of the docs, run `git worktree add docs gh-pages` from the project root. 
This makes any files written to the `docs` folder show up in the root of the `gh-pages` branch.

Within the main branch, the html documentation outputs are symlinked to this `docs` folder,
so everything will go into the correct part of the `gh-pages` branch assuming the worktree is setup.