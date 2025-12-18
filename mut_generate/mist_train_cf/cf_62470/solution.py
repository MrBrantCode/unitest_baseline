"""
QUESTION:
Write a function `filter_elements` that takes two numpy arrays, A and B, as input and returns a new array containing elements of A that are present in B. The solution should be efficient enough to handle large arrays (A of length approximately 3.8 million and B of length around 20k) without using a for loop. The output should be stored in a variable C.
"""

import numpy as np

def filter_elements(A, B):
    """
    Returns a new array containing elements of A that are present in B.

    Parameters:
    A (numpy array): The input array to be filtered.
    B (numpy array): The array containing the elements to filter by.

    Returns:
    numpy array: A new array containing elements of A that are present in B.
    """
    return A[np.in1d(A, B)]