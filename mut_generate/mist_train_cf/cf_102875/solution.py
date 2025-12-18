"""
QUESTION:
Write a function called "detect_outliers" that takes a list of integers as input and returns a boolean value indicating whether any outliers are present. The input list will have at least 3 integers. An outlier is defined as a value that is more than 2 standard deviations away from the mean of the dataset. The function should use the numpy library to calculate the mean and standard deviation.
"""

import numpy as np

def detect_outliers(lst):
    mean = np.mean(lst)
    std_dev = np.std(lst)
    outliers = [x for x in lst if abs(x - mean) > 2 * std_dev]
    return len(outliers) > 0