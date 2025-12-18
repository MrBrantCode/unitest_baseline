"""
QUESTION:
Write a function `generate_3d_array(l, m, n)` that takes three integers `l`, `m`, and `n` as input and returns a 3D array of size `l x m x n`. The array should be filled with numbers from 1 to `l*m*n` in a zig-zag pattern. The zig-zag pattern alternates between positive and negative directions along the third dimension (`n`) for each slice in the second dimension (`m`). The input values of `l`, `m`, and `n` should be restricted to integers between 1 and 5 (inclusive).
"""

import numpy as np

def generate_3d_array(l, m, n):
    """
    Generates a 3D array of size l x m x n filled with numbers from 1 to l*m*n in a zig-zag pattern.
    
    Parameters:
    l (int): The size of the first dimension. Should be between 1 and 5 (inclusive).
    m (int): The size of the second dimension. Should be between 1 and 5 (inclusive).
    n (int): The size of the third dimension. Should be between 1 and 5 (inclusive).
    
    Returns:
    numpy.ndarray: A 3D array of size l x m x n filled with numbers in a zig-zag pattern.
    """
    arr = np.empty((l, m, n), dtype=int)
    count = 1
    for k in range(l):
        for j in range(m):
            if j % 2 == 0:
                for i in range(n):
                    arr[k, j, i] = count
                    count += 1
            else:
                for i in range(n-1, -1, -1):
                    arr[k, j, i] = count
                    count += 1
    return arr