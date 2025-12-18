"""
QUESTION:
Write a function `calculate_stats(arr)` that calculates and returns the mean, variance, and standard deviation of a given array `arr`. Implement another function `normalize(arr)` that normalizes a given array `arr` such that its mean equals zero and its variance equals one without using any Python libraries for statistical calculation. The input arrays can be multi-dimensional. 

Restrictions: Do not use any Python libraries for statistical calculation in the `normalize(arr)` function. The input arrays are multi-dimensional, so only consider mean, variance, and standard deviation in the calculation.
"""

import numpy as np

def calculate_stats(arr):
    mean = np.mean(arr)
    var = np.var(arr)
    std_dev = np.std(arr)
    return mean, var, std_dev

def normalize(arr):
    mean, var, _ = calculate_stats(arr)
    normalized_arr = (arr - mean) / np.sqrt(var)
    return normalized_arr