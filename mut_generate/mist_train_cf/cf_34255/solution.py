"""
QUESTION:
Implement a function named `get_memory_size` that calculates the memory size of a given object in bytes. The function should take one argument `obj` of a standard Python data type (e.g., int, float, string, list, dictionary, etc.) and return its memory size in bytes.
"""

import sys

def get_memory_size(obj):
    """Return the memory size of the given object in bytes."""
    return sys.getsizeof(obj)