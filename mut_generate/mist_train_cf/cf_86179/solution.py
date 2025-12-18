"""
QUESTION:
Reshape a 2D numpy array into non-overlapping 2x2 sub-arrays. The function should take a 2D numpy array as input and return a 3D array or list where each 2x2 sub-array is a separate element. The output should preserve the original order of elements. The input array's dimensions must be divisible by 2.
"""

import numpy as np

def entrance(a):
    """
    Reshapes a 2D numpy array into non-overlapping 2x2 sub-arrays.
    
    Args:
    a (numpy.ndarray): 2D NumPy array with dimensions divisible by 2.
    
    Returns:
    numpy.ndarray: 3D NumPy array where each 2x2 sub-array is a separate element.
    """
    b = a.reshape(-1, 2, a.shape[1] // 2, 2)
    return b.transpose((0, 2, 1, 3)).reshape(-1, 2, 2)