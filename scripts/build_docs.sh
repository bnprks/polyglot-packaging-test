#!/usr/bin/env bash
set -eu

# Build per-language docs
for lang in cpp python r; do
    pushd $lang
    bash scripts/build_docs.sh
    popd
done

# Check the git worktree setup is good
if [ $(git branch --show-current) == "gh-pages" ] || [ $(cd docs; git branch --show-current) != "gh-pages" ]; then
    echo "Didn't detect proper git worktree in docs/ directory"
    echo "Please set this up by running: \"git worktree add docs gh-pages\""
fi

rm -r docs/r
cp -r r/docs docs/r

rm -r docs/cpp
cp -r cpp/docs/html/. docs/cpp

rm -r docs/python
cp -r python/docs/build/html/. docs/python

# Take the "links.html" file from Python and make it the global docs home
mv docs/python/links.html docs/index.html
sed -i 's|="_static|="python/_static|g' docs/index.html