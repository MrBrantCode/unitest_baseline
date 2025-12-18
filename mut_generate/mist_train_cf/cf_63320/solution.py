"""
QUESTION:
Design a function `min_max_normalise` that takes a list as input and returns a list of numerical values scaled to the range 0 to 1. The function should exclude non-numerical values and handle missing or NaN values. It should also avoid division by zero errors when the minimum and maximum values are the same.

Create another function `reverse_min_max_normalise` that takes a normalized list and the original list as input, and returns the original list of numerical values. This function should handle edge cases when the minimum and maximum values in the list are the same.
"""

import numpy as np

def min_max_normalise(lst):
    """Normalises list of numerical data to a range of 0 to 1. Excludes non-numerical data and handles missing/NaN values."""
    # Convert list to NumPy array and filter out non-numerical values
    arr = np.array(lst, dtype=float)
    
    # Filter out NaN values
    arr = arr[np.logical_not(np.isnan(arr))]

    # No division by zero error if min and max are the same
    if arr.min() != arr.max():
        normalised_arr = (arr - arr.min()) / (arr.max() - arr.min())
    else:
        normalised_arr = arr - arr.min()

    return normalised_arr.tolist()


def reverse_min_max_normalise(normalised_lst, original_lst):
    """Reverses the normalisation process and returns the original list of numerical data. Handles edge cases when the minimum and maximum values in the list are the same."""
    # Convert lists to NumPy arrays and filter out non-numerical and NaN values
    arr, original_arr = np.array(normalised_lst, dtype=float), np.array(original_lst, dtype=float)
    arr, original_arr = arr[np.logical_not(np.isnan(arr))], original_arr[np.logical_not(np.isnan(original_arr))]

    # No division by zero error if min and max in original list are the same
    if original_arr.min() != original_arr.max():
        denormalised_arr = arr * (original_arr.max() - original_arr.min()) + original_arr.min()
    else:
        denormalised_arr = arr + original_arr.min()

    return denormalised_arr.tolist()