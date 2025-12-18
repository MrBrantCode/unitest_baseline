"""
QUESTION:
Create a function `create_array` that constructs a Numpy array of shape 2x3 containing all instances of a specified integer value. The function should take an integer value as input and return the constructed Numpy array.
"""

import numpy as np

def create_array(value):
    """
    Construct a Numpy array of shape 2x3 containing all instances of a specified integer value.

    Args:
        value (int): The integer value to fill the array with.

    Returns:
        np.ndarray: A 2x3 Numpy array filled with the specified value.
    """
    return np.full((2, 3), value)