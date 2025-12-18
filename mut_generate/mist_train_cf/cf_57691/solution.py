"""
QUESTION:
Transform a 4-dimensional numpy array into a 3-dimensional array by reducing one dimension. The function should take a 4-dimensional numpy array as input and return a 3-dimensional numpy array. The reduction can be performed using any suitable numpy function such as sum, mean, max, or min, and it can be applied along any dimension of the input array. The function should be able to handle input arrays of any size.
"""

import numpy as np

def transform_array(array_4d, axis=-1):
    """
    Transform a 4-dimensional numpy array into a 3-dimensional array by reducing one dimension.

    Args:
    array_4d (numpy array): The input 4-dimensional numpy array.
    axis (int): The axis to reduce. Default is -1 (last dimension).

    Returns:
    array_3d (numpy array): The transformed 3-dimensional numpy array.
    """
    array_3d = np.sum(array_4d, axis=axis)
    return array_3d