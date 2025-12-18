"""
QUESTION:
Write a function `find_triplet_rows(matrix, target)` that finds three non-identical rows in a given matrix that sum up to a pre-specified target value. The function should return a tuple of the three rows if found, otherwise return None. The input matrix is a list of lists, where each inner list represents a row of numeric values. The target is an integer representing the desired sum.
"""

import itertools

def find_triplet_rows(matrix, target):
    """
    Finds three non-identical rows in a given matrix that sum up to a pre-specified target value.

    Args:
        matrix (list of lists): A list of lists, where each inner list represents a row of numeric values.
        target (int): The desired sum.

    Returns:
        tuple or None: A tuple of the three rows if found, otherwise None.
    """
    row_combinations = list(itertools.combinations(matrix, 3))
    for combination in row_combinations:
        sum_value = sum(sum(row) for row in combination)
        if sum_value == target:
            return combination
    return None