"""
QUESTION:
Create a function `invert_nested_tuple` that takes a nested tuple as input, inverts the numerical factors (both integers and floats) within the tuple, and returns the modified tuple. The function should recursively traverse the nested tuple structure, handle potential exceptions by ignoring non-numerical components, and avoid division by zero by returning zero if encountered.
"""

def invert_nested_tuple(t):
    """Invert numerical elements in a nested tuple."""
    if not isinstance(t, tuple):
        if isinstance(t, int) or isinstance(t, float):
            return 1.0 / t if t != 0 else t
        else:
            return t
    return tuple(invert_nested_tuple(i) for i in t)