"""
QUESTION:
Write a function called `detect_outliers` that identifies and isolates the outliers in a given set of integer data using the Z-score method. The function should take a list of integers as input and return a list of outliers. The threshold for determining an outlier is a Z-score greater than 2 standard deviations from the mean.
"""

import numpy as np

def detect_outliers(data):
    """
    Identify outliers in a given set of integer data using the Z-score method.

    Args:
        data (list): A list of integers.

    Returns:
        list: A list of outliers.
    """
    mean = np.mean(data)
    std_dev = np.std(data)
    threshold = 2  # for example..

    outliers = [i for i in data if np.abs((i - mean) / std_dev) > threshold]
    return outliers