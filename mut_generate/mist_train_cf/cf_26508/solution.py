"""
QUESTION:
Implement the `process_arrays` function that takes two 1-dimensional NumPy arrays `z1` and `z2` of the same length as input. The function should create a copy of `z2`, normalize `z2` by dividing each element by its maximum value, calculate the difference between `z1` and the normalized `z2` array, normalize the difference array, and set all negative values in the normalized difference array to 0. Return the copy of `z2`, the normalized `z2`, the unnormalized difference array, and the normalized difference array.
"""

import numpy as np

def process_arrays(z1, z2):
    z2_copy = np.copy(z2)
    z2_normalized = z2 / np.max(z2)
    difference = z1 - z2_normalized
    normalized_difference = (z1 - z2_normalized) / np.max(z1 - z2_normalized)
    normalized_difference[normalized_difference < 0] = 0
    return z2_copy, z2_normalized, difference, normalized_difference