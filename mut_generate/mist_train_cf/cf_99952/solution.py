"""
QUESTION:
Write a function named `find_min_max_values` that takes a 2D numpy array `dataset` as input, where each row represents a record and each column represents a numerical attribute. The function should return the minimum and maximum values for each attribute. The function should be efficient and scalable for large datasets.
"""

import numpy as np

def find_min_max_values(dataset):
    """
    This function takes a 2D numpy array as input and returns the minimum and maximum values for each attribute.
    
    Parameters:
    dataset (numpy array): A 2D numpy array where each row represents a record and each column represents a numerical attribute.
    
    Returns:
    min_values (numpy array): The minimum values for each attribute.
    max_values (numpy array): The maximum values for each attribute.
    """
    # Find the minimum value for each attribute
    min_values = np.amin(dataset, axis=0)
    # Find the maximum value for each attribute
    max_values = np.amax(dataset, axis=0)
    return min_values, max_values