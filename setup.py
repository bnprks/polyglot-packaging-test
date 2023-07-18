# Note: The actual package is in the python subdirectory. 
# This is just to help anyone who runs the wrong pip install command

error_msg = """\n
===============================================================================
ERROR: Incorrect installation command
To install polyglot-packaging-test, please run:
    pip install "git+https://github.com/bnprks/polyglot-packaging-test#subdirectory=python"
===============================================================================\n"""
raise Exception(error_msg)