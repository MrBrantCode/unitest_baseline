"""
QUESTION:
Write a function `string_to_array` that takes a comma-separated string of integers as input and returns a numpy array of integers. The function should use the `numpy.fromstring()` function with the `sep=','` and `dtype=int` arguments.
"""

import numpy as np

def string_to_array(s):
    return np.fromstring(s, dtype=int, sep=',')