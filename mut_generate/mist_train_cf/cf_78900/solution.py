"""
QUESTION:
Create a function `calculate_sums` that calculates the sum of each row, each column, and both diagonals of a given 2D array. The input array is a square matrix (i.e., the number of rows is equal to the number of columns), and the function should return the sum of each row, the sum of each column, and the sums of both diagonals.
"""

import numpy as np

def calculate_sums(array_2d):
    row_sums = np.sum(array_2d, axis=1)
    col_sums = np.sum(array_2d, axis=0)
    diag_sums_1 = np.trace(array_2d)
    diag_sums_2 = np.trace(np.flipud(array_2d))
    return row_sums, col_sums, diag_sums_1, diag_sums_2