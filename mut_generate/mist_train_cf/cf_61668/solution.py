"""
QUESTION:
Design a function named `compute_diff` that calculates the difference between the highest and lowest integers in a given array, along with their indices and the rounded mean of these two integers. The function should handle arrays containing duplicate or negative integers, and should also work with empty arrays. In case of multiple instances of the highest or lowest integer, the function should return the index of the first instance. The function should be efficient in terms of time and space complexity to handle arrays of up to 10^6 elements and up to 10^3 requests.
"""

import numpy as np

def compute_diff(array):
    if len(array) == 0:
        return "Array is empty"
    min_index = np.argmin(array)
    max_index = np.argmax(array)
    min_val = array[min_index]
    max_val = array[max_index]
    diff = max_val - min_val
    mean = round((max_val + min_val) / 2)
    return diff, min_index, max_index, mean