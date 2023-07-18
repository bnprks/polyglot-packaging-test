import pytest

import polyglotpackaging

def test_add():
    assert polyglotpackaging.py_add(1,2) == 3

def test_message():
    assert polyglotpackaging.py_message() == "Hello from C++!"