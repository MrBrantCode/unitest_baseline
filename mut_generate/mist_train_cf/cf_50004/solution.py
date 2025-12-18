"""
QUESTION:
Create a function `rotate_tensor` that takes a 3-dimensional tensor of size 3x3x3 as input, where the elements are integers ranging from 1 to 27. The function should rotate the tensor 90 degrees clockwise along the y-axis and return the rotated tensor. Assume the input tensor is a valid 3x3x3 numpy array.
"""

import numpy as np

def rotate_tensor(tensor):
    """
    Rotate a 3-dimensional tensor of size 3x3x3, 90 degrees clockwise along the y-axis.

    Parameters:
    tensor (numpy array): A 3-dimensional tensor of size 3x3x3.

    Returns:
    numpy array: The rotated tensor.
    """
    tensor_rotated = np.rot90(tensor, axes=(0, 2))
    return tensor_rotated