"""
QUESTION:
Write a function `one_hot_encode` that transforms a 1-dimensional numpy array of positive integers into a 2-dimensional one-hot array, where the leftmost element is always representative of 0. The function should use only numpy and be more efficient than iterating over the input array.

The input is a 1-dimensional numpy array of positive integers, and the output is a 2-dimensional numpy array. The size of the output array's second dimension is determined by the maximum value in the input array plus one.
"""

import numpy as np

def one_hot_encode(a):
    return np.eye(a.max()+1)[a]