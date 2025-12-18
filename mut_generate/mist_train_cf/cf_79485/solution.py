"""
QUESTION:
Design a function named `is_sorted` to verify if all elements in a given 2D numpy array are in ascending order both row-wise and column-wise. The input is a 2D numpy array and the output should be a boolean value indicating whether the array is sorted or not.
"""

def is_sorted(arr):
    import numpy as np

    # Sort rows
    sorted_rows = np.sort(arr, axis=1)

    # If sorted rows is not equal to original array return False
    if np.array_equal(sorted_rows, arr) is False:
        return False

    # Sort current sorted rows by column
    sorted_columns = np.sort(sorted_rows, axis=0)

    # If sorted columns is not equal to original array return False
    if np.array_equal(sorted_columns, arr) is False:
        return False

    # If it gets to this point, array is sorted in both rows and columns
    return True