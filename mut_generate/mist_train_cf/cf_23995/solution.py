"""
QUESTION:
Write a function `unwrap_tuple` that takes a nested tuple as input and returns the innermost value. The function should recursively traverse the tuple until it finds a non-tuple value. The input tuple may contain any number of nested tuples and the innermost value can be of any type.
"""

def unwrap_tuple(nested_tuple):
    if not isinstance(nested_tuple, tuple) or len(nested_tuple) != 1:
        return nested_tuple
    return unwrap_tuple(nested_tuple[0])