"""
QUESTION:
Calculate the Euclidean distance between two arrays of equal length using a function named `calculate_euclidean_distance`. The input arrays will be one-dimensional and contain integers. The function should take two arrays as input and return the Euclidean distance between them. Use numpy library for calculations.
"""

import numpy as np

def calculate_euclidean_distance(array1, array2):
    """
    Calculate the Euclidean distance between two arrays of equal length.

    Parameters:
    array1 (numpy array): The first array.
    array2 (numpy array): The second array.

    Returns:
    float: The Euclidean distance between the two arrays.
    """
    squared_diff = np.square(array1 - array2)
    sum_squared_diff = np.sum(squared_diff)
    euclidean_distance = np.sqrt(sum_squared_diff)
    return euclidean_distance