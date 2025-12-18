"""
QUESTION:
Write a function named `cov_sublists` that takes a list of numbers and an integer n as input. The function should calculate the coefficient of variation (standard deviation divided by mean) of every sub-list of n consecutive elements in the list and return or print these coefficients.
"""

import numpy as np

def cov_sublists(lst, n):
    return [np.std(sublist) / np.mean(sublist) for sublist in (lst[i:i+n] for i in range(len(lst) - n + 1))]