# Polyglot packaging test

This is a demo repository showcasing how to make a small C++ package
with bindings in both R and Python. The key feature is that the code
can be directly installed from the github source in both R and Python.

## Python installation
`pip install "git+https://github.com/bnprks/polyglot-packaging-test#subdirectory=python"`

## R installation
`remotes::install_github("bnprks/polyglot-packaging-test/r")`



## Documentation
The documentation site is built separately for each language, then combined into
a single static file tree in the top-level `docs` folder (not a tracked folder) .

For convenience with Github pages, the `gh-pages` branch
is mounted as the `docs` top-level folder using `git worktree add docs gh-pages`, then 
the documentation sites are combined into the top-level `docs` folder. This allows easy
deployment while keeping generated HTML files off of the main branch.

## R

 - Uses `pkgdown` with a standard setup
 - symlinks the docs directory into the output path
 - **Build**: `pkgdown::build_site()` from within the `r` directory

## Python

 - Uses Sphinx with the PyData theme
 - Includes a helper file with the overal project home page, linking to C++, R, and Python docs.
 - Files are automatically copied into place during the build process
 - **Build**: `make html` from within the `python/docs` directory

## C++

 - Uses Doxygen with the doxygene awesome css theme
 - Files are automatically copied into place during the build process
 - **Build**: `doxygen` from within the `cpp/docs` directory

### VS Code editing extensions

- Python: autoDocstring
- C++: Doxygen Documentation Generator
