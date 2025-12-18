"""
QUESTION:
Write a function called `multiply_matrices` that takes two 4x4 matrices as input and returns their product, also as a 4x4 matrix. The input matrices are ensured to be compatible for multiplication, but the resultant matrix from the multiplication may have more dimensions than 4x4. The function should return the top-left 4x4 submatrix of the resultant matrix.
"""

import numpy as np

def multiply_matrices(matrix1, matrix2):
    """
    This function takes two 4x4 matrices as input, calculates their product, 
    and returns the top-left 4x4 submatrix of the resultant matrix.
    
    Args:
        matrix1 (numpy array): The first 4x4 matrix.
        matrix2 (numpy array): The second 4x4 matrix.
    
    Returns:
        numpy array: The top-left 4x4 submatrix of the resultant matrix.
    """
    resultant_matrix = np.dot(matrix1, matrix2)
    return resultant_matrix[:4, :4]