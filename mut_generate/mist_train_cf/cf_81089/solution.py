"""
QUESTION:
Perform the following operations on two given 3x3 square matrices A and B. 

- Element-wise multiplication (Hadamard Product) of A and B.
- Compute the square of A and B separately using actual matrix multiplication.
- Find the eigenvalues and eigenvectors of both matrices A and B.
- Multiply A and B to get a third matrix C, and then compute the determinant of C.
- Extract the submatrices consisting of the first two rows and columns from both A and B, multiply the resulting submatrices, and compute the inverse of the result if it exists.

The results of the operations should be rounded off to 3 decimal places if the result is a float value. Ensure that the results are in a readable and well-formatted manner.
"""

import numpy as np
import numpy.linalg as la

def matrix_operations(A, B):
    """
    Perform various operations on two given 3x3 square matrices A and B.

    Args:
        A (numpy array): The first 3x3 square matrix.
        B (numpy array): The second 3x3 square matrix.

    Returns:
        A dictionary containing the results of the operations.
    """

    # Elementwise multiplication
    mul_elem = np.multiply(A, B)

    # Square of matrices
    A_sq = np.matmul(A, A)
    B_sq = np.matmul(B, B)

    # Eigenvalues and eigevectors
    values_A, vectors_A = la.eig(A)
    values_B, vectors_B = la.eig(B)

    # Multiply Matrices and find determinant
    C = np.matmul(A, B)
    det = la.det(C)

    # Submatrix multiplication and inverse
    A_sub = A[:2, :2]
    B_sub = B[:2, :2]
    mul_sub = np.matmul(A_sub, B_sub)
    
    try:
        inv_mul_sub = la.inv(mul_sub)
    except la.LinAlgError:
        inv_mul_sub = None

    # Round results to 3 decimal places
    results = {
        "Elementwise multiplication": np.round(mul_elem, 3),
        "Square of matrix A": np.round(A_sq, 3),
        "Square of matrix B": np.round(B_sq, 3),
        "Eigenvalues of A": np.round(values_A, 3),
        "Eigenvectors of A": np.round(vectors_A, 3),
        "Eigenvalues of B": np.round(values_B, 3),
        "Eigenvectors of B": np.round(vectors_B, 3),
        "Matrix C = A * B": np.round(C, 3),
        "Determinant of C": round(det, 3),
        "Multiplication of submatrices A and B": np.round(mul_sub, 3),
        "Inverse of the submatrix multiplication": np.round(inv_mul_sub, 3) if inv_mul_sub is not None else None,
    }

    return results