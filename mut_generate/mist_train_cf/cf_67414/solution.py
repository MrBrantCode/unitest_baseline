"""
QUESTION:
Write a function `identify_outliers` that takes a 1D numpy array `a` as input and returns a boolean array where True signifies an outlier and False indicates otherwise. An outlier is defined as a value that falls outside the interval (μ-2σ, μ+2σ), where μ is the mean and σ is the standard deviation of the input array.
"""

import numpy as np

def identify_outliers(a):
    """
    This function identifies outliers in a 1D numpy array.
    
    An outlier is defined as a value that falls outside the interval (μ-2σ, μ+2σ),
    where μ is the mean and σ is the standard deviation of the input array.
    
    Parameters:
    a (numpy array): A 1D numpy array.
    
    Returns:
    numpy array: A boolean array where True signifies an outlier and False indicates otherwise.
    """
    mean = np.mean(a)
    std_dev = np.std(a)
    lower_bound = mean - 2*std_dev
    upper_bound = mean + 2*std_dev
    
    return (a < lower_bound) | (a > upper_bound)