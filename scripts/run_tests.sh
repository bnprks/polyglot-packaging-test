#!/usr/bin/env bash
set -eu

for lang in cpp python r; do
    pushd $lang
    bash scripts/run_tests.sh
    popd
done