from .version import __version__
import polyglotpackaging.cpp

def py_add(a, b):
    """Add two numbers together

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of inputs
    """
    return polyglotpackaging.cpp.add(a, b)

def py_message():
    """Get a message from C++

    Returns:
        str: Message from C++
    """
    return polyglotpackaging.cpp.message()