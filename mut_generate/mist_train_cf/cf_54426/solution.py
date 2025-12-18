"""
QUESTION:
Write a function named `remove_uneven_elements` that takes a nested mixed tuple as input, removes all non-integer elements and the integer elements that are uneven, and returns the resulting tuple. The function should handle nested tuples of arbitrary depth.
"""

def remove_uneven_elements(nested_tuple):
    result = ()
    for i in nested_tuple:
        if type(i) is tuple:
            result += (remove_uneven_elements(i),)
        elif isinstance(i, int) and i % 2 == 0:
            result += (i,)
    return result