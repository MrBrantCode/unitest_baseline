"""
QUESTION:
Create a function called `deep_copy_array_of_arrays` that takes a numpy array of numpy arrays as input and returns a deep copy of the input array. The function should ensure that modifying the returned array does not affect the original array.
"""

import copy

def deep_copy_array_of_arrays(array_of_arrays):
    """
    Create a deep copy of the input array of numpy arrays.

    Args:
        array_of_arrays (numpy array of numpy arrays): The input array to be copied.

    Returns:
        numpy array of numpy arrays: A deep copy of the input array.
    """
    return copy.deepcopy(array_of_arrays)