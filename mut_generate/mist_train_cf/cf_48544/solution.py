"""
QUESTION:
Generate a function `generate_symmetric_matrix(vector)` that takes a 1D vector of integers as input and returns a symmetric square matrix where each element at position (i, j) is the product of the ith and jth elements of the input vector. The function should include error checking mechanisms to prevent array out of bounds errors and should have a space complexity of O(n^2), where n is the length of the input vector.
"""

import numpy as np

def generate_symmetric_matrix(vector):
    """
    Generate a symmetric square matrix from a 1D vector of integers.
    
    Each element at position (i, j) is the product of the ith and jth elements of the input vector.
    
    Args:
    vector (list): A 1D vector of integers.
    
    Returns:
    np.ndarray: A symmetric square matrix.
    """
    
    n = len(vector)
    
    # Create an empty n x n matrix
    matrix = np.zeros((n, n))
    
    # Populate the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i, j] = vector[i] * vector[j]
            matrix[j, i] = matrix[i, j]
            
    return matrix