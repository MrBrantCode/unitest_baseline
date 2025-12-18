"""
QUESTION:
Implement a Python function named `calculate_statistics` that takes a list of numbers as input and calculates the mean and standard deviation of the numbers. The function should also calculate the frequency distribution of the numbers and return all the results. The input list will contain at least one number, and all numbers in the list will be unique integers.
"""

import numpy as np
from collections import Counter

def calculate_statistics(numbers):
    """
    Calculate the mean, standard deviation, and frequency distribution of the given numbers.

    Args:
    numbers (list): A list of unique integers.

    Returns:
    tuple: A tuple containing the mean, standard deviation, and frequency distribution.
    """
    # Calculate the mean
    mean = np.mean(numbers)
    # Calculate the standard deviation
    std_dev = np.std(numbers)
    # Calculate the frequency distribution
    freq_dist = dict(Counter(numbers))
    return mean, std_dev, freq_dist