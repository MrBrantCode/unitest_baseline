"""
QUESTION:
Extract the nth element from a 2D numpy array in row-major order without flattening the array. The function should be named 'extract_nth_element' and should take two parameters: a 2D numpy array and the index 'n' of the desired element (1-indexed).
"""

import numpy as np

def extract_nth_element(arr, n):
    """
    Extract the nth element from a 2D numpy array in row-major order.

    Parameters:
    arr (numpy.ndarray): A 2D numpy array.
    n (int): The 1-indexed position of the element to extract.

    Returns:
    The nth element in the array.
    """
    counter = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            counter += 1
            if counter == n:
                return arr[i][j]