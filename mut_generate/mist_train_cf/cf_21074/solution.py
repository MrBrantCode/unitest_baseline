"""
QUESTION:
Create a function named `sum_odd_or_less_than_10` that takes a 2D numpy array as input. The array must have at least 2 rows and 3 columns and contain only positive integers. This function should return the sum of all elements in the array that are not divisible by 2 or are less than or equal to 10.
"""

import numpy as np

def sum_odd_or_less_than_10(arr: np.ndarray) -> int:
    """
    This function calculates the sum of all elements in a 2D numpy array 
    that are not divisible by 2 or are less than or equal to 10.

    Args:
        arr (np.ndarray): A 2D numpy array with at least 2 rows and 3 columns.

    Returns:
        int: The sum of all elements in the array that meet the conditions.
    """
    # Filter out elements that are divisible by 2 and greater than 10
    filtered_arr = arr[(arr % 2 != 0) | (arr <= 10)]

    # Compute the sum of all remaining elements
    return np.sum(filtered_arr)