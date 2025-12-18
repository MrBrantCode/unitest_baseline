"""
QUESTION:
Write a function `normalize_array(arr)` that takes a 2D numpy array as input and returns a new 2D array where all values range between 0 and 1. The function should handle edge cases where all values in the input array are zero or where the maximum and minimum values in the array are the same.
"""

import numpy as np

def normalize_array(arr):
    # calculate the minimum and maximum of the array
    max_val = arr.max()
    min_val = arr.min()
    
    # edge case: all values in array are zero, return array as is
    if max_val == 0 and min_val == 0:
        return arr
    # edge case: max value is the same as the min value
    # (all values in array are the same)
    elif max_val == min_val:
        return np.ones_like(arr)
    
    # subtract the minimum from all elements and divide by the range
    normalized = (arr - min_val) / (max_val - min_val)
    return normalized