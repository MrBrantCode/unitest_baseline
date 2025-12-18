"""
QUESTION:
Create a function `largest_indices` that takes a numpy array `a` and an integer `N` as input. The function should return a numpy array containing the indices of the N largest elements in `a`, arranged in descending order. The function should use numpy's `argsort` method to achieve this.
"""

import numpy as np

def largest_indices(a, N):
    """
    Returns the indices of the N largest elements in a numpy array.

    Parameters:
    a (numpy array): Input array.
    N (int): Number of largest elements to return.

    Returns:
    numpy array: Indices of the N largest elements in descending order.
    """
    return a.argsort()[-N:][::-1]