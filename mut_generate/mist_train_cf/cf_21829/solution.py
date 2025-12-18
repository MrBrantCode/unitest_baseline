"""
QUESTION:
Write a function called `matrix_multiplication` that takes two matrices M1 and M2 as input and returns their product if the number of columns in M1 is equal to the number of rows in M2. If not, it should output an error message. The function should also calculate the determinant of the resulting matrix and return both the matrix and the determinant value. The function should work for matrices of size at least 3x3.
"""

import numpy as np

def matrix_multiplication(M1, M2):
    """
    This function performs matrix multiplication and calculates the determinant of the resulting matrix.
    
    Args:
        M1 (list): The first input matrix.
        M2 (list): The second input matrix.
    
    Returns:
        tuple: A tuple containing the product matrix and its determinant value.
    """
    # Check if the number of columns in M1 is equal to the number of rows in M2
    if len(M1[0]) != len(M2):
        print("Error: The number of columns in M1 is not equal to the number of rows in M2.")
        return None
    
    # Perform matrix multiplication
    result = [[0] * len(M2[0]) for _ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                result[i][j] += M1[i][k] * M2[k][j]
    
    # Calculate the determinant of the resulting matrix
    determinant = np.linalg.det(result)
    
    return result, determinant