"""
QUESTION:
Create a function named `process_4d_array` that takes a 4x4x4x4 four-dimensional array as input. The function should process each element in the array considering all four dimensions. Implement the processing logic inside the function.
"""

import numpy as np

def process_4d_array(array_4d):
    """
    Process a 4x4x4x4 four-dimensional array by multiplying each element by 2.

    Parameters:
    array_4d (numpy.ndarray): A 4x4x4x4 four-dimensional array.
    """
    for i in range(array_4d.shape[0]):
        for j in range(array_4d.shape[1]):
            for k in range(array_4d.shape[2]):
                for l in range(array_4d.shape[3]):
                    array_4d[i, j, k, l] *= 2  # modification: multiply each number by 2
    return array_4d