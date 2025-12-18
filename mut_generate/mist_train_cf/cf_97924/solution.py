"""
QUESTION:
Create a function named `remove_outliers` that takes in a 1-dimensional numpy array `data` and an optional parameter `threshold` with a default value of 1.5. The function should return a new array containing only the values from `data` that are within a certain range defined by the interquartile range (IQR) and the given threshold. Specifically, the range should be between Q1 - `threshold` * IQR and Q3 + `threshold` * IQR, where Q1 and Q3 are the 25th and 75th percentiles of `data`, respectively.
"""

import numpy as np

def remove_outliers(data, threshold=1.5):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return data[(data > lower_bound) & (data < upper_bound)]