"""
QUESTION:
Construct a function named `find_str` that takes two arguments: `info`, a list of distinct-length lists, and a string `y`. Return a list of tuples representing the index positions where `y` occurs within `info`, in the format (row, index). If `y` appears multiple times within the same list, the tuples should be arranged in ascending order of index. The function should handle cases where `y` does not occur in `info` and where `info` is an empty list.
"""

def find_str(info, y):
    return [(i, j) for i, row in enumerate(info) for j, elem in enumerate(row) if elem == y]