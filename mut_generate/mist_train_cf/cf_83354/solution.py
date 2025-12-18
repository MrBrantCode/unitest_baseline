"""
QUESTION:
Write a function named `reshape_into_5D_array` that takes a one-dimensional array and five dimensions (u, t, p, m, n) as input, and returns the reshaped five-dimensional array. If the reshaping is not possible due to invalid dimensions, return an error message. Additionally, write a helper function named `flatten_5D_array` that takes a five-dimensional array as input and returns its one-dimensional representation.
"""

import numpy as np

def reshape_into_5D_array(array, u, t, p, m, n):
    try:
        return np.array(array).reshape(u, t, p, m, n).tolist()
    except:
        return "Cannot reshape. Invalid dimensions."