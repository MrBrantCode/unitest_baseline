"""
QUESTION:
Write a function `calculate_statistics` that takes a list of numbers as input and returns the mean, standard deviation, and frequency distribution of the numbers. The function should use the numpy library to calculate the mean and standard deviation, and the collections library to calculate the frequency distribution. The function should return the results in the specified format. The input list will contain only integers.
"""

import numpy as np
from collections import Counter

def calculate_statistics(numbers):
    """
    Calculate the mean, standard deviation, and frequency distribution of a list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the mean, standard deviation, and frequency distribution.
    """
    mean = np.mean(numbers)
    std_dev = np.std(numbers)
    freq_dist = dict(Counter(numbers))
    return mean, std_dev, freq_dist