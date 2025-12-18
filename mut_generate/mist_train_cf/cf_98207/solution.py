"""
QUESTION:
Write a function named `modified_roll` that shifts a subset of elements in a NumPy array along a specified axis using `np.roll()`, applies a specified mathematical operation to the shifted array, and returns the modified array. The function should take the input array, shift values, axis to shift along, mathematical operation, and any additional operation arguments as input parameters.
"""

import numpy as np

def modified_roll(arr, shifts, axis, op=None, *args, **kwargs):
    shifted_arr = np.roll(arr, shifts, axis=axis)
    if op is not None:
        shifted_arr = op(shifted_arr, *args, **kwargs)
    return shifted_arr