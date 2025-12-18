"""
QUESTION:
Write a function named `subtract_matrices` that takes two 2D matrices as input and returns their difference. The matrices are guaranteed to have the same dimensions. The function should handle the matrices as individual accounts of two-dimensional data structures and return the result as a 2D matrix where each element is the difference of corresponding elements in the input matrices.
"""

def subtract_matrices(matrix1, matrix2):
    """
    This function takes two 2D matrices as input and returns their difference.
    
    Args:
        matrix1 (list): The first 2D matrix.
        matrix2 (list): The second 2D matrix.
    
    Returns:
        list: A 2D matrix where each element is the difference of corresponding elements in the input matrices.
    """
    num_rows = len(matrix1)
    num_cols = len(matrix1[0])
    result = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    
    for i in range(num_rows):
        for j in range(num_cols):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    
    return result