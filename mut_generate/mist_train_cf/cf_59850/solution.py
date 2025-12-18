"""
QUESTION:
Write a function called `multiply_and_check` that takes two 3D square matrices `Mat1` and `Mat2` as input. The function should first check if `Mat1` and `Mat2` are orthogonal by verifying if their dot product with their transpose is an identity matrix. Then, it should multiply the two matrices and calculate the determinant of the resulting matrix. The function should return a boolean indicating whether both input matrices are orthogonal, the resulting matrix after multiplication, and the determinant of the resulting matrix. The input matrices should have the same shape.
"""

import numpy as np

def multiply_and_check(Mat1, Mat2):
    """
    This function checks if two input matrices are orthogonal, 
    multiplies the two matrices and calculates the determinant 
    of the resulting matrix.

    Args:
    Mat1 (numpy array): A 3D square matrix.
    Mat2 (numpy array): A 3D square matrix.

    Returns:
    bool: A boolean indicating whether both input matrices are orthogonal.
    numpy array: The resulting matrix after multiplication.
    float: The determinant of the resulting matrix.
    """

    # Check if matrices are orthogonal
    is_orthogonal = np.allclose(np.dot(Mat1, Mat1.T), np.eye(Mat1.shape[0]), atol=1e-8) and np.allclose(np.dot(Mat2, Mat2.T), np.eye(Mat2.shape[0]), atol=1e-8)

    # Perform the multiplication
    Result = np.dot(Mat1, Mat2)

    # Calculate the determinant
    Det = np.linalg.det(Result)

    return is_orthogonal, Result, Det