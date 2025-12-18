"""
QUESTION:
Write a function `has_duplicate_pairs` that checks for duplicate pairs in a multi-dimensional array. A pair consists of two consecutive elements in a sub-array. The function should return `True` if it finds a duplicate pair, and `False` otherwise. The input array can contain sub-arrays of varying lengths.
"""

def has_duplicate_pairs(array):
    seen = set()
    for sub_array in array:
        for pair in zip(sub_array, sub_array[1:]):
            if pair in seen:
                return True
            seen.add(pair)
    return False