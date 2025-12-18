"""
QUESTION:
Create a function called `pad_array` that takes a 2D numpy array, a target shape, and a padding element as input, and returns a new 2D numpy array with the input array padded to the target shape by adding the padding element to the right and bottom. The padding should be done in a way that the original array remains at the top left of the resulting array.

The function should be able to handle arrays of varying dimensions and should be efficient enough to be applied to thousands of rows. The target shape and the padding element are given, but the dimensions of the input array may vary.
"""

import numpy as np

def pad_array(array, target_shape, padding_element):
    """
    Pads a 2D numpy array to a target shape by adding a padding element to the right and bottom.

    Args:
        array (numpy.ndarray): The input 2D numpy array.
        target_shape (tuple): The target shape of the output array.
        padding_element (int or float): The element used for padding.

    Returns:
        numpy.ndarray: The padded 2D numpy array.
    """
    padding_width = ((0, target_shape[0] - array.shape[0]), (0, target_shape[1] - array.shape[1]))
    return np.pad(array, padding_width, mode='constant', constant_values=padding_element)