"""
QUESTION:
Create a function `get_size_of_array(arr)` that calculates the size of a multi-dimensional array in bytes. Implement another function `resize_array(arr, new_shape)` to dynamically resize the array to a new shape while preserving its contents. Additionally, create a function `validate_data_integrity(original, resized)` to verify the integrity of the data in the array after resizing. 

Assume the array is a numpy array. The functions should work for any given numpy array. The time and space complexity of the solution should be analyzed and provided.
"""

import sys
import numpy as np

def get_size_of_array(arr):
    """Get size of numpy array in bytes."""
    return sys.getsizeof(arr)

def resize_array(arr, new_shape):
    """Return copy of original array resized to new_shape, preserving data."""
    return np.resize(arr, new_shape)

def validate_data_integrity(original, resized):
    """Validate data of resized array is the same as original up to its length."""
    return np.array_equal(original.flatten()[:resized.size], resized.flatten())