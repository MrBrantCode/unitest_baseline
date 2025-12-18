"""
QUESTION:
Create a function named `validate_array` that takes a 5x5 2D array as input, where the first row contains integers from 1 to 5, the second row contains integers from 6 to 10, and so on. The function should validate that the sum of elements in each row, column, and diagonal is equal and return a message indicating whether the validation passed or failed.
"""

import numpy as np

def validate_array(arr):
    """
    Validate that the sum of elements in each row, column, and diagonal is equal.

    Args:
    arr (numpy.ndarray): A 5x5 2D array.

    Returns:
    str: A message indicating whether the validation passed or failed.
    """

    # Sum of elements in each row
    row_sums = np.sum(arr, axis=1)
    # Sum of elements in each column
    col_sums = np.sum(arr, axis=0)
    # Sum of elements in the diagonals
    diag_sum1 = np.trace(arr)
    diag_sum2 = np.trace(np.fliplr(arr))

    # Check if all sums are equal
    if len(set(row_sums)) == 1 and len(set(col_sums)) == 1 and diag_sum1 == diag_sum2 == row_sums[0] == col_sums[0]:
        return "Validation Passed: Sums of all rows, columns and diagonals are equal!"
    else:
        return "Validation Failed: Sums are not equal."