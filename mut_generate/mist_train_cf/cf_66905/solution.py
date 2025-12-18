"""
QUESTION:
Create a function `check_sum_trio(matrix, targetSum)` that checks if there exists a trio of unique rows in a given matrix where the summation of their elements equals a pre-determined figure `targetSum`. The function should return `True` if such a trio exists, and `False` otherwise. The matrix is represented as a 2D list of integers, and the `targetSum` is an integer.
"""

import numpy as np
import itertools

def check_sum_trio(matrix, targetSum):
    rows = np.array(matrix).reshape(len(matrix), -1)
    combinations = list(itertools.combinations(rows, 3))
    for trio in combinations:
        if np.sum(trio) == targetSum:
            return True
    return False