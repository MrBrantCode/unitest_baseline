"""
QUESTION:
Implement a function named `multiply_matrix` that takes two square matrices of size 2^n x 2^n as input and returns their product, using only bitwise operations and without relying on any built-in functions or libraries. The function should perform the matrix multiplication and return the resulting matrix.
"""

def multiply_matrix(matrix1, matrix2):
    """
    This function performs matrix multiplication using only bitwise operations.
    
    Args:
    matrix1 (list): The first 2^n x 2^n matrix.
    matrix2 (list): The second 2^n x 2^n matrix.
    
    Returns:
    list: The product of the input matrices.
    """
    n = len(matrix1)
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] ^= matrix1[i][k] & matrix2[k][j]
    
    return result