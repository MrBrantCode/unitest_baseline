"""
QUESTION:
Write a function named `string_to_numpy_array` that takes a comma-separated string of integers as input and returns a numpy array of integers. The function must be able to handle strings with any number of integers, and the integers can be positive, negative, or zero. Use the `numpy.fromstring()` function to achieve this transformation efficiently.
"""

import numpy as np

def string_to_numpy_array(int_string):
    return np.fromstring(int_string, dtype=int, sep=',')