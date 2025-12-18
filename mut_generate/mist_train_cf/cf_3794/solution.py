"""
QUESTION:
Write a function `calculate_stats` that takes a list of numbers as input, removes any outliers that are 3 standard deviations away from the mean, replaces them with the mean value of the remaining data set, and returns the mean and median of the modified data set.
"""

import numpy as np

def calculate_stats(data):
    """
    This function takes a list of numbers, removes any outliers that are 3 standard deviations away from the mean, 
    replaces them with the mean value of the remaining data set, and returns the mean and median of the modified data set.

    Args:
        data (list): A list of numbers.

    Returns:
        tuple: A tuple containing the mean and median of the modified data set.
    """

    mean = np.mean(data)
    std_dev = np.std(data)
    threshold = 3 * std_dev

    data_no_outliers = [mean if abs(x - mean) > threshold else x for x in data]
    mean_no_outliers = np.mean(data_no_outliers)
    median_no_outliers = np.median(data_no_outliers)

    return mean_no_outliers, median_no_outliers