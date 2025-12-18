"""
QUESTION:
Write a function named `count_black_pixels` that takes an RGB image array as input and returns the total count of black pixels in the image, where black is represented as [0, 0, 0]. The solution should use a vector-based approach and avoid iterating over rows and columns.
"""

import numpy as np

def count_black_pixels(img_array):
    """
    Count the total number of black pixels in an RGB image array.
    
    Parameters:
    img_array (numpy.ndarray): RGB image array.
    
    Returns:
    int: Total count of black pixels in the image.
    """
    return np.count_nonzero(np.all(img_array == [0, 0, 0], axis=-1))