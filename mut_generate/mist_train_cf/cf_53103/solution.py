"""
QUESTION:
Construct a function `secondary_diagonal` that takes a square bi-dimensional matrix as input and returns its secondary diagonal. The secondary diagonal is defined as the diagonal that starts at the top right corner and ends at the bottom left corner of the matrix. The function should work for any square matrix of size n x n, where n is a positive integer.
"""

def secondary_diagonal(matrix):
    """
    This function takes a square bi-dimensional matrix as input and returns its secondary diagonal.
    
    Parameters:
    matrix (list): A square bi-dimensional matrix.
    
    Returns:
    list: The secondary diagonal of the input matrix.
    """
    return [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]