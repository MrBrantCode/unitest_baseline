"""
QUESTION:
Write a function named `solve` that calculates the coefficient of variation of a given list of floating point numbers, discards any outlier (any value more than two standard deviations from the mean), and then recalculates the coefficient of variation. The list must have more than two elements, otherwise return an error message.
"""

import numpy as np

def solve(lst):
    if len(lst) < 3:  
        return "List must have more than two elements"

    # calculate mean
    mean = np.mean(lst)

    # calculate standard deviation
    std_dev = np.std(lst)

    # calculate coefficient of variation
    original_coef_of_var = std_dev / mean

    # discard any outlier (any value more than two standard deviations from the mean)
    lst = [i for i in lst if (mean - 2 * std_dev) < i < (mean + 2 * std_dev)]

    # calculate new coefficient of variation
    new_mean = np.mean(lst)
    new_std_dev = np.std(lst)
    new_coef_of_var = new_std_dev / new_mean

    return original_coef_of_var, new_coef_of_var