"""
QUESTION:
Write a function named sort_array_np that sorts a given array using numpy. The function should be able to handle multidimensional arrays and have the ability to sort along a specified axis. The axis parameter should be optional and default to 0 if not provided.
"""

import numpy as np
def sort_array_np(array, axis=0):
    return np.sort(array, axis)