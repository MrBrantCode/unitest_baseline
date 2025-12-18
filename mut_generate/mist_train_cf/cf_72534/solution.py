"""
QUESTION:
Create a function `normalize_data` that scales an 8x5 numpy array to a range of 0-1. The function should then be used to normalize the data, and the mean, median, mode, range, variance, and standard deviation should be calculated before and after normalization.
"""

import numpy as np

def normalize_data(data):
    min_data = np.min(data, axis=None)
    max_data = np.max(data, axis=None)
    return (data - min_data) / (max_data - min_data)