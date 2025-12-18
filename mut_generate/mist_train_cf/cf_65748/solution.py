"""
QUESTION:
Implement a function called `batch_normalization` that applies batch normalization to the input data. The function should take in a 2D array representing the input data and return the normalized data. The batch normalization process involves standardizing the inputs to have zero mean and unit variance. Assume the input data is a mini-batch of samples from a larger dataset, where each column represents a feature and each row represents a sample.
"""

import numpy as np

def batch_normalization(data):
    """
    Applies batch normalization to the input data.

    Args:
    data (numpy.ndarray): A 2D array representing the input data.

    Returns:
    normalized_data (numpy.ndarray): The normalized data.
    """
    # Calculate the mean of each column (feature)
    mean = np.mean(data, axis=0)
    
    # Subtract the mean from each column to center the data
    centered_data = data - mean
    
    # Calculate the variance of each column
    variance = np.var(data, axis=0)
    
    # Avoid division by zero
    variance = np.maximum(variance, 1e-5)
    
    # Normalize the centered data by dividing by the square root of the variance
    normalized_data = centered_data / np.sqrt(variance)
    
    return normalized_data