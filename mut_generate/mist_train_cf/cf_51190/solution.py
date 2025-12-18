"""
QUESTION:
Create a function called `normalize_array` that takes a numerical array as input and returns the array with its elements normalized to have a mean of 0 and a standard deviation of 1. The function should calculate the mean and standard deviation of the input array and apply the standardization formula (subtracting the mean and dividing by the standard deviation) to each element. The original array should not be modified.
"""

import numpy as np

def normalize_array(array):
    array = np.array(array)
    array_mean = np.mean(array)
    array_std = np.std(array)

    return (array - array_mean) / array_std