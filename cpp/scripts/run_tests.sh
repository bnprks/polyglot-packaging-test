#!/usr/bin/env bash
set -eu

cmake -S . -B build

pushd build
    make
    ctest
popd