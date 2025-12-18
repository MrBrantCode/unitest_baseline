"""
QUESTION:
Implement a function `get_sum_dim_2` that takes a 2D numpy array and returns the sum of elements along rows and columns without using numpy's built-in sum function. The function should also identify the row and column with the maximum sum without using numpy's built-in max function. The function should return four values: a list of row sums, a list of column sums, the index of the row with the maximum sum, and the index of the column with the maximum sum.
"""

import numpy as np

def get_sum_dim_2(arr):
    row_sums = []
    col_sums = []

    # Compute the sum of elements along rows
    for row in arr:
        row_sum = 0
        for elem in row:
            row_sum += elem
        row_sums.append(row_sum)

    # Compute the sum of elements along columns
    for col in zip(*arr):
        col_sum = 0
        for elem in col:
            col_sum += elem
        col_sums.append(col_sum)

    # Find which row and column yield the maximum sum
    max_row_sum_idx = row_sums.index(max(row_sums))
    max_col_sum_idx = col_sums.index(max(col_sums))

    return row_sums, col_sums, max_row_sum_idx, max_col_sum_idx