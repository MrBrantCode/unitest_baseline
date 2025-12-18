"""
QUESTION:
Write a function called `calculate_standard_deviation` that takes a 1D numpy array of numbers as input and returns the standard deviation of the array. The function must calculate the standard deviation in two steps: first, calculate the mean of the array, and then use this mean to compute the variance, which is used in the standard deviation formula.
"""

import numpy as np

def calculate_standard_deviation(data):
    # Calculate the mean
    mean = np.mean(data)

    # Compute the variance
    variance = np.mean((data - mean)**2)

    # Calculate the standard deviation
    std_dev = np.sqrt(variance)
    
    return std_dev