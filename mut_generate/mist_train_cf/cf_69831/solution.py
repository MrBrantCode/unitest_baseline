"""
QUESTION:
Write a function `element_wise_mul` that takes two matrices as input, multiplies them element-wise, and returns the result. If the input matrices have different dimensions, treat the missing elements in the smaller matrix as ones. The function should also handle edge cases where the inputs are non-numeric.
"""

import numpy as np

def element_wise_mul(mat1, mat2):
    try:
        mat1 = np.array(mat1)
        mat2 = np.array(mat2)
    except Exception as e:
        return "Error: The inputs should be either lists or numpy arrays"
        
    try:
        if mat1.shape != mat2.shape:
            max_shape = np.maximum(mat1.shape, mat2.shape)

            result_mat1 = np.ones(max_shape, dtype=np.float32)
            result_mat2 = np.ones(max_shape, dtype=np.float32)

            result_mat1[tuple(map(slice, mat1.shape))] = mat1
            result_mat2[tuple(map(slice, mat2.shape))] = mat2

            mat1 = result_mat1
            mat2 = result_mat2

        return mat1 * mat2
    except Exception as e:
        return f"Error: {str(e)}"