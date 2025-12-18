"""
QUESTION:
Create a function called `min_disparity(matrix)` that calculates the smallest disparity (absolute difference) between any pair of elements in a given 2D matrix. The matrix can be of any size and the disparity can be between elements in the same row, same column, or diagonally. If the input matrix is empty, the function should return 'Error!!! Matrix is empty'.
"""

import numpy as np

def min_disparity(matrix):
    if not matrix.size:
        return 'Error!!! Matrix is empty'

    flat_list = matrix.flatten()
    flat_list_sorted = np.sort(flat_list)

    min_diff = float('inf')
    for i in range(1, len(flat_list_sorted)):
        if flat_list_sorted[i] - flat_list_sorted[i-1] < min_diff:
            min_diff = flat_list_sorted[i] - flat_list_sorted[i-1]

    return min_diff