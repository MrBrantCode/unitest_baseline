"""
QUESTION:
Write a function `find_attribute_extremes` that takes a 2D NumPy array as input, where each row represents a record and each column represents a numerical attribute. The function should return two NumPy arrays, one containing the highest values for each attribute and another containing the lowest values for each attribute. Use the NumPy library to achieve this efficiently.
"""

import numpy as np

def find_attribute_extremes(dataset):
    """
    This function takes a 2D NumPy array as input, where each row represents a record 
    and each column represents a numerical attribute. It returns two NumPy arrays, 
    one containing the highest values for each attribute and another containing the 
    lowest values for each attribute.

    Parameters:
    dataset (numpy.ndarray): A 2D NumPy array.

    Returns:
    tuple: A tuple of two NumPy arrays. The first array contains the highest values 
    for each attribute, and the second array contains the lowest values for each 
    attribute.
    """
    # Find the highest value for each attribute
    max_values = np.amax(dataset, axis=0)
    # Find the lowest value for each attribute
    min_values = np.amin(dataset, axis=0)
    return max_values, min_values