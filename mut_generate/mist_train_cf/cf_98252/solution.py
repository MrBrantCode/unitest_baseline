"""
QUESTION:
Write a function `calculate_mean_median_std_dev` that takes a list of numbers as input and returns a list containing the mean, median, and standard deviation of the input list.
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