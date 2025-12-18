"""
QUESTION:
Write a function `convert_array_to_list` that takes a NumPy array as input, sorts its elements in descending order, and converts them to a list. The function should have a time complexity of O(n log n), where n is the number of elements in the array.
"""

import numpy as np

def convert_array_to_list(array):
    sorted_array = np.sort(array, axis=None)[::-1]
    converted_list = sorted_array.tolist()
    return converted_list