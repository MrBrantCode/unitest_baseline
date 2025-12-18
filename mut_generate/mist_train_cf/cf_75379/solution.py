"""
QUESTION:
Create a function `matrix_operations(matrix)` that accepts a square matrix, calculates its transpose and inverse, and performs addition, subtraction, and multiplication operations between the original and transposed matrix. The function should validate the input matrix and handle cases where the matrix is not square or singular, returning an error message in such cases.
"""

import numpy as np

def matrix_operations(matrix):
    """
    This function accepts a square matrix, calculates its transpose and inverse, 
    and performs addition, subtraction, and multiplication operations between the original and transposed matrix.

    Args:
    matrix (list): A 2D list representing a square matrix.

    Returns:
    None or str: Returns error messages if the matrix is not square or singular.
    """
    try:
        matrix = np.array(matrix)
        if matrix.shape[0] != matrix.shape[1]:
            return "The input matrix is not a square matrix."

        # calculating the transpose of the matrix
        transposed_matrix = matrix.T

        # calculating the inverse of the matrix
        inverse_matrix = np.linalg.inv(matrix)

        # performing addition operation
        addition_result = np.add(matrix, transposed_matrix)

        # performing subtraction operation
        subtraction_result = np.subtract(matrix, transposed_matrix)

        # performing multiplication operation
        multiplication_result = np.dot(matrix, transposed_matrix)

        return {
            "Transposed Matrix": transposed_matrix,
            "Inverse Matrix": inverse_matrix,
            "Addition of Matrix and Transposed Matrix": addition_result,
            "Subtraction between Matrix and Transposed Matrix": subtraction_result,
            "Multiplication of Matrix and Transposed Matrix": multiplication_result
        }
        
    except np.linalg.LinAlgError:
        return "The input matrix is singular, it does not have an inverse."