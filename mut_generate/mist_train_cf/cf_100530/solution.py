"""
QUESTION:
Implement a function `modified_roll` that shifts a subset of elements in a given array along a specified axis using the NumPy `np.roll()` function, applies a mathematical operation to the shifted array, and returns the result. The function should take the input array, a tuple of shift values, the axis to shift along, and an optional mathematical operation as input parameters.
"""

import numpy as np

def modified_roll(arr, shifts, axis, op=None, *args, **kwargs):
    shifted_arr = np.roll(arr, shifts, axis=axis)
    if op is not None:
        shifted_arr = op(shifted_arr, *args, **kwargs)
    return shifted_arr