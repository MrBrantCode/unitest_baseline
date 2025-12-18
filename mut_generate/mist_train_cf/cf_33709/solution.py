"""
QUESTION:
Implement a function `input_data` that takes a numpy array `data` as input, standardizes the data using the Z-score method so that it has a mean of 0 and a standard deviation of 1, and returns the standardized data. The function should use NumPy to calculate the mean and standard deviation of the input data.
"""

import numpy as np

def input_data(data: np.ndarray) -> np.ndarray:
    """
    Standardize the input data using the Z-score method.

    Parameters:
    data : numpy.ndarray
        The input data to be standardized.

    Returns:
    numpy.ndarray
        The standardized data.
    """

    mean = np.mean(data)
    std_dev = np.std(data)
    standardized_data = (data - mean) / std_dev
    return standardized_data