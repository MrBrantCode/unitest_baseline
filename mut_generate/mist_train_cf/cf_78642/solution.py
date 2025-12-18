"""
QUESTION:
Create a function named `windowed_view` that takes a 1D numpy array `a` and an integer `window_length` as input. The function should return a 2D numpy array where each row represents a window of `window_length` consecutive elements from the input array `a`. The first row should start from the first element of `a`, and each subsequent row should start one element after the previous row, stopping when there are not enough elements left to fill a full window. The function should be implemented in a way that minimizes memory usage and avoids explicit looping.
"""

import numpy as np
from numpy.lib.stride_tricks import as_strided

def windowed_view(a, window_length):
    """
    Create a 2D numpy array where each row represents a window of consecutive elements from the input array.

    Parameters:
    a (numpy array): 1D numpy array
    window_length (int): length of the window

    Returns:
    numpy array: 2D numpy array where each row represents a window of consecutive elements from the input array
    """
    shape = (a.size - window_length + 1, window_length)
    strides = (a.itemsize, a.itemsize)
    return as_strided(a, shape=shape, strides=strides)