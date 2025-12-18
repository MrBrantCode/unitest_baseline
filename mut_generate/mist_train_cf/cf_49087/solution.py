"""
QUESTION:
Create a function `generate_spiral(n)` that generates an `n x n` matrix with values from 1 to `n^2` in a spiral pattern. The function should use NumPy and return the generated matrix. The matrix should be filled in the order of left to right, top to bottom, right to left, and bottom to top for each layer of the matrix.
"""

import numpy as np

def generate_spiral(n):
    matrix = np.zeros((n, n))
    number = 1
    for layer in range((n + 1) // 2):
        for ptr in range(layer, n - layer):  
            matrix[layer, ptr] = number
            number += 1
        for ptr in range(layer + 1, n - layer):  
            matrix[ptr, -(layer + 1)] = number
            number += 1
        for ptr in range(layer + 1, n - layer):  
            matrix[-(layer + 1), -(ptr + 1)] = number
            number += 1
        for ptr in range(layer + 1, n - (layer + 1)):  
            matrix[-(ptr + 1), layer] = number
            number += 1
    return matrix