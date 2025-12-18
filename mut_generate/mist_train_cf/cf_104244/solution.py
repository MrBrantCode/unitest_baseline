"""
QUESTION:
Write a function called "detect_outliers" that takes in a list of integers and returns a boolean value indicating if any outliers are present or not. The input list will have at least 5 integers. An outlier is defined as a value that is more than 3 standard deviations away from the mean of the dataset. The function should use the numpy library to calculate the mean and standard deviation.
"""

import numpy as np

def detect_outliers(data):
    mean = np.mean(data)
    std = np.std(data)
    threshold = 3 * std

    for value in data:
        if abs(value - mean) > threshold:
            return True
    
    return False