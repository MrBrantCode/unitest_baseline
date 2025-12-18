"""
QUESTION:
Create a function `get_isometric_lists` that takes a list of NumPy arrays `arrays`, an integer `limit_width`, and a fill value `fill_value` as input, and returns a new list of isometric lists. Each isometric list should have a fixed width of `limit_width`, padding with `fill_value` if the original array is shorter, or truncating if the original array is longer. The function should return a list of these transformed isometric lists.
"""

import numpy as np

def get_isometric_lists(arrays, limit_width, fill_value):
    isometric_arrays = []
    for array in arrays:
        if len(array) < limit_width:
            padded_array = np.pad(array, (0, limit_width - len(array)), constant_values=fill_value)
            isometric_arrays.append(padded_array)
        else:
            truncated_array = array[:limit_width]
            isometric_arrays.append(truncated_array)
    return isometric_arrays