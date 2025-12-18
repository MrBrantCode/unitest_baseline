"""
QUESTION:
Implement a function `compare_num(a, b, c=None)` that compares two numbers `a` and `b`, and returns -1 if `a` is less than `b`, 0 if they are equal, and 1 if `a` is greater than `b`. If an optional parameter `c` is provided, the function should return the sum of the compared results of `a` with `b` and `a` with `c`. The function should handle edge cases where `a`, `b`, or `c` is not an integer or float, in which case it should return `None`.
"""

def compare_num(a, b, c=None):
    # check if a, b, and c are numeric
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return None
    if c is not None and not isinstance(c, (int, float)):
        return None

    compare = lambda x, y: -1 if x < y else (0 if x == y else 1)

    if c is None:
        return compare(a, b)
    else:
        return compare(a, b) + compare(a, c)