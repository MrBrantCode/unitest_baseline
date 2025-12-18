"""
QUESTION:
Write a function `compute_determinant(matrix)` that takes a 2D list of numbers (including integers and decimals) as input and returns the determinant of the matrix, rounded to two decimal places. If the input matrix is not square, the function should return an error message. The function should be able to handle large matrices but may be limited by system resources.
"""

import numpy as np

def compute_determinant(matrix):
    try:
        # Convert to numpy array to utilize numpy methods
        matrix = np.array(matrix)
        
        # Check if matrix is square
        if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
            return "Error: Matrix is not square"
        
        # Use numpy's linlag.det method to compute determinant
        return round(np.linalg.det(matrix), 2)
    
    except Exception as e:
        return str(e)