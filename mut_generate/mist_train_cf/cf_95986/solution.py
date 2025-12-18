"""
QUESTION:
Write a function `detect_outliers(arr)` that takes an array of at least 20 elements and returns a list of outliers. An outlier is defined as a value that is either greater than 5 times the interquartile range (IQR) above the third quartile or less than 5 times the IQR below the first quartile.
"""

import numpy as np

def detect_outliers(arr):
    q1 = np.percentile(arr, 25)
    q3 = np.percentile(arr, 75)
    iqr = q3 - q1
    threshold = 5 * iqr
    outliers = [num for num in arr if num > (q3 + threshold) or num < (q1 - threshold)]
    return outliers