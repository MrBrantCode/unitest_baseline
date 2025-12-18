"""
QUESTION:
Write a function `calculate_statistics` that takes a list of numbers as input and calculates the range, interquartile range (IQR), and standard deviation of the data. The function should return the calculated values. 

The input list should contain at least one number, and the function should be able to handle a list of any size. The input list will only contain integers or floats. 

The function should use the `numpy` library to perform calculations.
"""

import numpy as np

def calculate_statistics(data):
    """
    Calculate the range, interquartile range (IQR), and standard deviation of the data.

    Parameters:
    data (list): A list of numbers.

    Returns:
    tuple: A tuple containing the range, interquartile range, and standard deviation of the data.
    """
    # calculate range
    range_val = np.ptp(data)

    # calculate interquartile range
    q75, q25 = np.percentile(data, [75, 25])
    iqr = q75 - q25

    # calculate standard deviation
    std_dev = np.std(data)

    return range_val, iqr, std_dev