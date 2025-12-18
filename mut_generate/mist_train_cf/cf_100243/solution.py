"""
QUESTION:
Implement a Python function named `array_operations` that takes a 2D NumPy array as input. The function should be able to perform the following operations on the array: get the shape of the array, reshape the array, concatenate the array with another array, split the array into sub-arrays, and flatten the array. The function should return a dictionary containing the results of each operation. 

The function should include the following parameters: `arr` (the input 2D NumPy array), `new_shape` (the new shape for the reshape operation), `arr_to_concat` (the array to concatenate with the input array), `axis_to_concat` (the axis along which to concatenate the arrays), `split_indices` (the indices along which to split the array), and `axis_to_split` (the axis along which to split the array). 

The function should return a dictionary with the following keys: 'shape', 'reshaped', 'concatenated', 'split', and 'flattened'.
"""

import numpy as np

def array_operations(arr, new_shape, arr_to_concat, axis_to_concat, split_indices, axis_to_split):
    """
    Perform various operations on a 2D NumPy array.

    Parameters:
    arr (numpy.ndarray): The input 2D NumPy array.
    new_shape (tuple): The new shape for the reshape operation.
    arr_to_concat (numpy.ndarray): The array to concatenate with the input array.
    axis_to_concat (int): The axis along which to concatenate the arrays.
    split_indices (list): The indices along which to split the array.
    axis_to_split (int): The axis along which to split the array.

    Returns:
    dict: A dictionary containing the results of each operation.
    """

    # Get the shape of the array
    shape = arr.shape

    # Reshape the array
    reshaped = arr.reshape(new_shape)

    # Concatenate the array with another array
    concatenated = np.concatenate((arr, arr_to_concat), axis=axis_to_concat)

    # Split the array into sub-arrays
    split = np.split(arr, split_indices, axis=axis_to_split)

    # Flatten the array
    flattened = arr.flatten()

    # Return a dictionary containing the results of each operation
    return {
        'shape': shape,
        'reshaped': reshaped,
        'concatenated': concatenated,
        'split': split,
        'flattened': flattened
    }