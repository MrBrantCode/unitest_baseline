"""
QUESTION:
Create a function `matrix_multiplication(A, B)` that takes two matrices `A` and `B` as input and returns their product. The function should handle the potential error where the number of columns in `A` does not match the number of rows in `B`. The function should also round the result to 4 decimal places. The input matrices will be square matrices with random elements having up to 4 decimal places, generated using NumPy's `np.random.rand()` function. The function should return an error message if the matrix multiplication is not possible due to a mismatch in dimensions.
"""

import numpy as np

def matrix_multiplication(A, B):
    """
    This function multiplies two matrices A and B. It first checks if the number of columns in A 
    matches the number of rows in B. If not, it returns an error message. If the matrices can be 
    multiplied, it returns their product rounded to 4 decimal places.

    Args:
        A (numpy array): The first matrix
        B (numpy array): The second matrix

    Returns:
        numpy array or str: The product of A and B if they can be multiplied, otherwise an error message
    """
    if A.shape[1] != B.shape[0]:
        return "Error: The number of columns in the first matrix must match the number of rows in the second matrix."
    
    return np.round(np.dot(A, B), 4)