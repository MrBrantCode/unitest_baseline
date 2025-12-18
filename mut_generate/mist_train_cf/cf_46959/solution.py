"""
QUESTION:
Create a function called `create_mask` that creates a boolean mask to select specific columns in a 64x64 array. The function should take a list of column indices as input and return a 64x64 boolean array where the specified columns are set to `True` and all other elements are set to `False`. The function should be able to handle a list of up to 10 column indices.
"""

import numpy as np

def create_mask(cols_to_mask):
    """
    Creates a boolean mask to select specific columns in a 64x64 array.

    Parameters:
    cols_to_mask (list): A list of column indices to be set to True in the mask.

    Returns:
    numpy.ndarray: A 64x64 boolean array where the specified columns are set to True.
    """
    mask = np.zeros((64,64), dtype=bool)
    mask[:, cols_to_mask] = True
    return mask