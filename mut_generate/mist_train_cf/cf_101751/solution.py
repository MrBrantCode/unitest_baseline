"""
QUESTION:
Given a 2D array of numerical values, write a function `find_extreme_values` that returns the highest and lowest values for each column in the array. The function should use the NumPy library and be able to handle arrays with any number of rows and columns.
"""

import numpy as np

def find_extreme_values(dataset):
    """
    This function takes a 2D numpy array as input and returns the highest and lowest values for each column.

    Parameters:
    dataset (numpy.ndarray): A 2D array of numerical values.

    Returns:
    tuple: A tuple containing two numpy arrays. The first array contains the highest values for each column, 
           and the second array contains the lowest values for each column.
    """
    max_values = np.amax(dataset, axis=0)
    min_values = np.amin(dataset, axis=0)
    return max_values, min_values