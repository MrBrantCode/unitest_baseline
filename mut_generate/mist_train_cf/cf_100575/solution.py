"""
QUESTION:
Create a function named `calculate_mean_median_std_dev` that takes a list of numbers (vector) as input, calculates the mean, median, and standard deviation of the vector, stores these values in a list in the order of mean, median, and standard deviation, and returns this list. The function should use the NumPy library for calculating the median and standard deviation.
"""

import numpy as np

def calculate_mean_median_std_dev(vector):
    # calculate mean of the vector
    mean = sum(vector) / len(vector)

    # calculate median of the vector using numpy
    median = np.median(vector)

    # calculate standard deviation of the vector using numpy
    std_dev = np.std(vector)

    # store all three values in a list
    result = [mean, median, std_dev]

    # return the list containing all three values
    return result