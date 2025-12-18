"""
QUESTION:
Write a function `calculate_second_std_dev` that takes a 1D numpy array as input and returns a tuple containing the lower and upper bounds of the 2nd standard deviation interval, calculated as (μ-2σ, μ+2σ), where μ is the mean and σ is the standard deviation of the input array.
"""

import numpy as np

def calculate_second_std_dev(a):
    """
    Calculate the lower and upper bounds of the 2nd standard deviation interval.

    Parameters:
    a (numpy array): 1D input array.

    Returns:
    tuple: A tuple containing the lower and upper bounds of the 2nd standard deviation interval.
    """
    mean_a = np.mean(a)
    std_a = np.std(a)
    lower_bound = mean_a - 2 * std_a
    upper_bound = mean_a + 2 * std_a
    return (lower_bound, upper_bound)