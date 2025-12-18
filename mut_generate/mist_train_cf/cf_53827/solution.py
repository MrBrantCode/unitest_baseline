"""
QUESTION:
Create a function `weighted_average(numbers, weights)` that calculates the weighted average of the given numbers using the corresponding weights. The function should use numpy for array operations, but not for the actual weighted average calculation. The input arrays `numbers` and `weights` should be of the same length, and the sum of all weights should be 1.0.
"""

import numpy as np

def weighted_average(numbers, weights):
    """
    Calculate the weighted average of the given numbers using the corresponding weights.

    Args:
    numbers (np.array): The array of numbers.
    weights (np.array): The array of weights. The sum of all weights should be 1.0.

    Returns:
    float: The weighted average of the given numbers.
    """
    return np.sum(numbers * weights)