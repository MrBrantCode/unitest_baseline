"""
QUESTION:
Write a function named `flatten` that takes a multi-dimensional matrix as input and returns its one-dimensional flattened version. The function should be optimized for space usage and computational complexity, and it should be extensible to matrices of four or more dimensions.
"""

from functools import reduce

def flatten(matrix):
    if not isinstance(matrix, list):
        return [matrix]
    else:
        return reduce(lambda x, y: x + flatten(y), matrix, [])