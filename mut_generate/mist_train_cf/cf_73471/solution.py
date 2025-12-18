"""
QUESTION:
Implement a function named `minkowski_distance` that calculates the Minkowski distance between two multi-dimensional numpy arrays `array_1` and `array_2` with a given integer `p`. Ensure the function includes validation checks for array sizes and datatype. The function should accept two 2D numpy arrays of equal shape and an integer `p` that is at least 1.
"""

import numpy as np

def minkowski_distance(array_1, array_2, p):
    """
    Calculate the Minkowski distance between two multi-dimensional numpy arrays.
    
    Parameters:
    array_1 (numpy.ndarray): First multi-dimensional array.
    array_2 (numpy.ndarray): Second multi-dimensional array.
    p (int): The order of the Minkowski distance (p >= 1).
    
    Returns:
    float: The Minkowski distance between array_1 and array_2.
    """
    
    # Validate inputs
    assert type(array_1) == np.ndarray, "Input array 1 is not numpy ndarray"
    assert type(array_2) == np.ndarray, "Input array 2 is not numpy ndarray"
    assert array_1.shape == array_2.shape, "Input arrays must be of same shape"
    assert type(p) == int, "p must be integer"
    assert p >= 1, "p must be at least 1"
    
    # Calculate Minkowski distance
    return np.sum(np.abs(array_1 - array_2)**p)**(1/p)