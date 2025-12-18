"""
QUESTION:
Create a function `determinant(matrix)` that calculates the determinant of a given n x n matrix. The function should be able to handle any square matrix of size n x n and return an error message if the input matrix is not square (m x n where m ≠ n). The function should strive for optimized time complexity.
"""

import numpy as np

def determinant(matrix):
    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        return "Error: Matrix is not square"

    # Convert to NumPy array for easier manipulation
    np_matrix = np.array(matrix)

    # Calculate and return determinant
    det = np.linalg.det(np_matrix)
    
    return det