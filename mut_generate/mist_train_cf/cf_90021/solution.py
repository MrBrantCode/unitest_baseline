"""
QUESTION:
Create a function called `multiply_matrices` that takes two 4x4 matrices as input and returns their product. The function should not use any built-in matrix multiplication functions.
"""

def multiply_matrices(mat1, mat2):
    """
    This function multiplies two 4x4 matrices and returns their product.
    
    Parameters:
    mat1 (list): The first 4x4 matrix.
    mat2 (list): The second 4x4 matrix.
    
    Returns:
    list: The product of the two input matrices.
    """
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    # Multiply matrices and store the result in the 'result' matrix
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result