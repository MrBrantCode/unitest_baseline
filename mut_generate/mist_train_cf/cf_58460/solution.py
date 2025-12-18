"""
QUESTION:
Write a function `matrix_operations` that takes a 3x3 matrix as input and returns the original matrix, its transpose, and a new matrix with squared elements. The function should not use any external libraries.
"""

def matrix_operations(matrix):
    """
    This function takes a 3x3 matrix as input, 
    and returns the original matrix, its transpose, 
    and a new matrix with squared elements.

    Args:
        matrix (list of lists): A 3x3 matrix.

    Returns:
        tuple of lists of lists: A tuple containing the original matrix, 
        its transpose, and a new matrix with squared elements.
    """
    # Transpose of the matrix:
    transpose_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    # New matrix with squared elements:
    squared_matrix = [[elem**2 for elem in row] for row in matrix]
    
    return matrix, transpose_matrix, squared_matrix