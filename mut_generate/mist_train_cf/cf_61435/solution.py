"""
QUESTION:
Write a function `array_size_discrepancy` that takes a numpy array as input and returns a boolean indicating whether the `nbytes` attribute of the array matches the actual memory usage estimated by `sys.getsizeof`. The function should not take any other parameters and should not perform any I/O operations.
"""

import numpy as np
import sys

def array_size_discrepancy(arr):
    """
    Checks if the nbytes attribute of a numpy array matches the actual memory usage estimated by sys.getsizeof.

    Parameters:
    arr (numpy array): The input numpy array.

    Returns:
    bool: True if the nbytes attribute matches the actual memory usage, False otherwise.
    """
    return arr.nbytes == sys.getsizeof(arr)