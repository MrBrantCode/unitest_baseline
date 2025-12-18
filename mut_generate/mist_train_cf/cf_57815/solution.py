"""
QUESTION:
Create a function `array_difference` that takes two numpy arrays A and B as input. The function should return a new array C containing all the elements of A that are not present in B. The function should not use a for loop to reduce computational time. The arrays A and B can be large, with sizes up to 3.8 million and 20,000 respectively.
"""

import numpy as np

def array_difference(A, B):
    """
    Returns a new array containing all the elements of A that are not present in B.

    Parameters:
    A (numpy array): The first input array.
    B (numpy array): The second input array.

    Returns:
    numpy array: A new array containing all the elements of A that are not present in B.
    """
    return A[~np.in1d(A, B)]

# For very large arrays, consider using numpy.lib.arraysetops.in1d with assume_unique=True
def array_difference_optimized(A, B):
    """
    Returns a new array containing all the elements of A that are not present in B.

    Parameters:
    A (numpy array): The first input array.
    B (numpy array): The second input array.

    Returns:
    numpy array: A new array containing all the elements of A that are not present in B.
    """
    return A[~np.in1d(A, B, assume_unique=True)]