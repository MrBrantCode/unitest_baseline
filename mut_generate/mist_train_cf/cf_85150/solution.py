"""
QUESTION:
Implement a function `compare_tuples(t1, t2)` that compares two tuples `t1` and `t2` and returns a new tuple where each element is the difference between the corresponding elements of `t1` and `t2`. If an element in `t1` or `t2` is a tuple itself, the function should recursively call itself to compare the inner tuples. If an element is not a number, it should be treated as 0. If one tuple is longer than the other, the function should pad the shorter tuple with its median value until they are the same length.
"""

from statistics import median

def compare_tuples(t1, t2):
    """
    Compare two tuples and return a new tuple with differences between corresponding elements.
    If an element is a tuple, recursively call compare_tuples. If an element is not a number, treat it as 0.
    If one tuple is longer than the other, pad the shorter tuple with its median value.

    Args:
        t1 (tuple): The first tuple to compare.
        t2 (tuple): The second tuple to compare.

    Returns:
        tuple: A new tuple with differences between corresponding elements.
    """

    def recurse_convert(tup):
        return tuple(recurse_convert(i) if isinstance(i, tuple) else 0 if not isinstance(i, (int, float)) else i for i in tup)

    def pad_tuple(t1, t2):
        if len(t1) > len(t2):
            median_val = median(t2) if len(t2) else 0
            t2 += (median_val,) * (len(t1) - len(t2))
        elif len(t2) > len(t1):
            median_val = median(t1) if len(t1) else 0
            t1 += (median_val,) * (len(t2) - len(t1))
        return t1, t2

    t1, t2 = recurse_convert(t1), recurse_convert(t2)
    t1, t2 = pad_tuple(t1, t2)

    def helper(x, y):
        if isinstance(x, tuple) and isinstance(y, tuple):
            return compare_tuples(x, y)
        else:
            return x - y if isinstance(x, (int, float)) and isinstance(y, (int, float)) else x if isinstance(x, (int, float)) else y if isinstance(y, (int, float)) else 0

    return tuple(helper(x, y) for x, y in zip(t1, t2))