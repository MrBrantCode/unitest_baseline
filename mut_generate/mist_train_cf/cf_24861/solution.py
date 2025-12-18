"""
QUESTION:
Write a function `transpose_matrix` that takes a 2D array as input and returns the transposed matrix. The function should return a new 2D array where the rows of the original matrix are the columns of the new matrix and vice versa. The input matrix is a list of lists where each inner list has the same length.
"""

def transpose_matrix(matrix):
    """
    This function takes a 2D array as input and returns the transposed matrix.
    
    Args:
    matrix (list of lists): A 2D array where each inner list has the same length.
    
    Returns:
    list of lists: A new 2D array where the rows of the original matrix are the columns of the new matrix and vice versa.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]