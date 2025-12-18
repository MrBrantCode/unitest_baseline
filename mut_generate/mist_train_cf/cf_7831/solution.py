"""
QUESTION:
Write a function `convert_array_to_list` that takes a NumPy array as input. The function should flatten the array if it has multiple dimensions, sort the elements in descending order, and return the result as a list. The function should have a time complexity of O(n log n), where n is the number of elements in the array.
"""

import numpy as np

def convert_array_to_list(array):
    """
    This function takes a NumPy array, flattens it if it has multiple dimensions, 
    sorts the elements in descending order, and returns the result as a list.

    Args:
        array (numpy.ndarray): The input NumPy array.

    Returns:
        list: A sorted list of elements from the input array in descending order.
    """
    if len(array.shape) > 1:
        flattened_array = array.flatten()
    else:
        flattened_array = array
    sorted_array = np.sort(flattened_array)[::-1]
    converted_list = sorted_array.tolist()
    return converted_list