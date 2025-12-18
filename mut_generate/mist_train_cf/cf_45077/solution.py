"""
QUESTION:
Create a function named `zero_pad_array` that takes two parameters: `array` (the input array) and `target_shape` (the target shape to which the input array should be padded). The function should zero-pad the input array to match the `target_shape`, padding equally on the left and right, as well as the top and bottom. If an equal distribution is not possible, allocate the remaining row/column to the bottom/right.
"""

import numpy as np

def zero_pad_array(array, target_shape):
    """
    Zero-pads the input array to match the target shape.

    Args:
        array (numpy.ndarray): The input array to be padded.
        target_shape (tuple): The target shape to which the input array should be padded.

    Returns:
        numpy.ndarray: The zero-padded array.
    """
    # Calculate the padding required on each side
    pad_top = (target_shape[0] - array.shape[0]) // 2
    pad_bottom = target_shape[0] - array.shape[0] - pad_top
    pad_left = (target_shape[1] - array.shape[1]) // 2
    pad_right = target_shape[1] - array.shape[1] - pad_left

    # Apply padding
    return np.pad(array, ((pad_top, pad_bottom), (pad_left, pad_right)))