"""
QUESTION:
Create a function `matrix_multiply` that multiplies two 4x4 matrices and returns the result matrix. The function should take two 4x4 matrices as input and return a new 4x4 matrix where each element is the sum of the products of corresponding elements from the rows of the first matrix and the columns of the second matrix.
"""

def matrix_multiply(mat1, mat2):
    """
    This function multiplies two 4x4 matrices and returns the result matrix.
    
    Args:
        mat1 (list): The first 4x4 matrix.
        mat2 (list): The second 4x4 matrix.
    
    Returns:
        list: A new 4x4 matrix where each element is the sum of the products of corresponding elements from the rows of the first matrix and the columns of the second matrix.
    """
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    # matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result