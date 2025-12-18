"""
QUESTION:
Write a function named `calculate_weighted_average` that takes a 2D array of numbers and a corresponding weight array as input. The function should flatten the 2D array into a 1D array, normalize the weights so they sum up to 1, and then calculate the weighted average.
"""

import numpy as np

def calculate_weighted_average(matrix, weights):
    """
    Calculate the weighted average of a 2D array after flattening and normalizing the weights.

    Args:
    matrix (numpy array): A 2D array of numbers.
    weights (numpy array): A corresponding weight array.

    Returns:
    float: The weighted average of the flattened array.
    """
    flattened = matrix.flatten()
    weights = weights / weights.sum()
    return np.average(flattened, weights=weights)