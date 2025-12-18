"""
QUESTION:
Construct a function `replace_sevens(matrix)` that takes a 2D numpy array as input, replaces all integers in the array that are either divisible by 7 or contain the digit 7 with -1, and returns the modified array along with the count of -1s. The function should be versatile enough to handle numerical 2D arrays of varying dimensions.
"""

import numpy as np

def replace_sevens(matrix):
    matrix[(matrix%7 == 0) | np.isin(matrix // 10, 7) | np.isin(matrix % 10, 7)] = -1
    return matrix, np.sum(matrix == -1)