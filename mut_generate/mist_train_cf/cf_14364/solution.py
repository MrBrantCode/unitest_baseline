"""
QUESTION:
Write a function named `sort_and_convert_to_list` that takes a NumPy array as input. The function should sort the elements of the array in descending order and return them as a list. The input array can be multi-dimensional.
"""

import numpy as np

def sort_and_convert_to_list(array):
    sorted_array = np.sort(array, axis=None)[::-1]
    return sorted_array.tolist()