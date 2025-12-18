"""
QUESTION:
Create a function `create_2d_array` to encapsulate a two-dimensional array or matrix in Python. The function should efficiently manipulate data and minimize memory usage. Use a data structure suitable for scientific computation, allowing operations to be performed over the entire array without the need for for loops.
"""

import numpy as np

def create_2d_array(rows, cols, val=None):
    """
    Creates a 2D array of a specified size with optional default value.
    
    Args:
        rows (int): Number of rows in the array.
        cols (int): Number of columns in the array.
        val (int, optional): Default value to fill the array with. Defaults to None.
    
    Returns:
        np.ndarray: A 2D NumPy array.
    """
    return np.full((rows, cols), val)