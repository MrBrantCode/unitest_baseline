"""
QUESTION:
Write a function `normalize_data` that takes a list of numbers as input and returns a list with the same numbers normalized to have a mean of 0 and a standard deviation of 1. The function should not take any other parameters.
"""

import numpy as np

def normalize_data(data):
    return (data - np.mean(data)) / np.std(data)