"""
QUESTION:
Create a function `list_difference` that takes two lists `a` and `b` as input and returns a list of elements present in `a` but not in `b`. The function should not modify the original lists and should only include each unique element from `a` that is not found in `b` in its output.
"""

def list_difference(a, b):
    """Returns a list of elements present in `a` but not in `b`."""
    return [x for x in a if x not in b]