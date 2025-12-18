"""
QUESTION:
Create a function named `validate_and_multiply` that takes three 3D matrices as input and returns their element-wise multiplication as a list if all matrices have the same dimensions. If the matrices do not have the same dimensions, return an error message. The input matrices are in the form of 3D lists.
"""

import numpy as np

def validate_and_multiply(mat1, mat2, mat3):
    # Convert the lists to numpy arrays
    np_mat1 = np.array(mat1)
    np_mat2 = np.array(mat2)
    np_mat3 = np.array(mat3)

    # Check if the dimensions of the 3 matrices are same
    if np_mat1.shape == np_mat2.shape == np_mat3.shape:
        # Perform elementwise multiplication
        result = np_mat1 * np_mat2 * np_mat3
        return result.tolist()
    else:
        return "Error: The matrices do not have the same dimensions."