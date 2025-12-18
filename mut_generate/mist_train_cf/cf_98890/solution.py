"""
QUESTION:
Find the highest and lowest values for each attribute in a 2D numerical dataset. 

Create a function named `find_max_min_values` that takes a 2D NumPy array as input and returns two NumPy arrays containing the highest and lowest values for each attribute (column) in the dataset. The function should use the NumPy library and should be efficient for large datasets.
"""

import numpy as np

def find_max_min_values(dataset):
    """
    Find the highest and lowest values for each attribute in a 2D numerical dataset.

    Args:
        dataset (numpy.ndarray): A 2D NumPy array representing the dataset.

    Returns:
        tuple: Two NumPy arrays containing the highest and lowest values for each attribute.
    """
    max_values = np.amax(dataset, axis=0)
    min_values = np.amin(dataset, axis=0)
    return max_values, min_values