"""
QUESTION:
Create a function `calculate_euclidean_distance` that calculates the Euclidean distance between two input arrays of the same length. Each element in the array is a number between 0 and 100,000. The function should return the Euclidean distance.
"""

import numpy as np

def calculate_euclidean_distance(array1, array2):
    """
    Calculate the Euclidean distance between two input arrays of the same length.

    Args:
        array1 (numpy array): The first input array.
        array2 (numpy array): The second input array.

    Returns:
        float: The Euclidean distance between the two arrays.
    """
    squared_diff = np.square(array1 - array2)
    sum_squared_diff = np.sum(squared_diff)
    euclidean_distance = np.sqrt(sum_squared_diff)
    return euclidean_distance