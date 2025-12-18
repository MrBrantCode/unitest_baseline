"""
QUESTION:
Create a function called `calculate_sum_squared_deviations_and_std_dev` that takes a 2D array as input and returns the summation of squared deviations between each integer in the array and the arithmetic mean of the array, along with the standard deviation of the array. Use NumPy for calculations. The input array will contain integers.
"""

import numpy as np

def calculate_sum_squared_deviations_and_std_dev(array):
    """
    Calculate the summation of squared deviations and the standard deviation of a given 2D array.

    Parameters:
    array (numpy.ndarray): A 2D array containing integers.

    Returns:
    tuple: A tuple containing the summation of squared deviations and the standard deviation.
    """

    # Calculate the mean of the array
    mean = np.mean(array)

    # Calculate the squared deviations
    squared_deviations = (array - mean)**2

    # Summation of squared deviations
    sum_squared_deviations = np.sum(squared_deviations)

    # Standard deviation
    std_dev = np.std(array)

    return sum_squared_deviations, std_dev