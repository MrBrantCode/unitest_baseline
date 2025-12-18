"""
QUESTION:
Create a function `calculate_statistics` that takes a list of numbers as input and returns the mean, standard deviation, and frequency distribution of the numbers. The function should use the `numpy` library to calculate the mean and standard deviation, and the `collections` library to calculate the frequency distribution. The function should return the results in a format that can be easily printed or further processed.
"""

import numpy as np
from collections import Counter

def calculate_statistics(data):
    """
    Calculate the mean, standard deviation, and frequency distribution of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        A dictionary with the mean, standard deviation, and frequency distribution of the numbers.
    """
    mean = np.mean(data)
    std_dev = np.std(data)
    freq_dist = dict(Counter(data))
    return {
        "Mean": mean,
        "Standard Deviation": std_dev,
        "Frequency Distribution": freq_dist
    }