"""
QUESTION:
Write a function `multiply_matrices` that takes two 4x4 matrices `mat1` and `mat2` as input, multiplies them, and returns the resulting 4x4 matrix. The function should not use any built-in matrix multiplication functions and instead perform the multiplication manually using nested loops.
"""

def multiply_matrices(mat1, mat2):
    """
    This function multiplies two 4x4 matrices manually using nested loops.
    
    Args:
        mat1 (list): The first 4x4 matrix.
        mat2 (list): The second 4x4 matrix.
    
    Returns:
        list: The resulting 4x4 matrix.
    """
    
    # Initialize the result matrix with zeros
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