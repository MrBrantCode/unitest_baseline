"""
QUESTION:
Create a function `is_array_in_list` that checks if a given numpy array is a member of a list of numpy arrays. The function should take two parameters: a numpy array `c` and a list of numpy arrays `CNTS`. It should return `True` if `c` is a member of `CNTS`, and `False` otherwise. The function should handle the case where `c` is identical to an array in `CNTS` but the comparison using the `in` keyword raises a ValueError.
"""

import numpy as np

def is_array_in_list(c, CNTS):
    """
    Checks if a given numpy array is a member of a list of numpy arrays.

    Parameters:
    c (numpy array): The numpy array to check.
    CNTS (list of numpy arrays): The list of numpy arrays.

    Returns:
    bool: True if c is a member of CNTS, False otherwise.
    """
    return any([np.array_equal(c, cnt) for cnt in CNTS])