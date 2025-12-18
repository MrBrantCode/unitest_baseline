"""
QUESTION:
Create a function called `transpose_matrix` that takes a 3x3 bi-dimensional matrix as input and returns its mathematical transpose. The function must validate the input to ensure it is a perfect 3x3 square matrix. The input matrix is a list of lists where each inner list represents a row in the matrix, and each element in the inner list represents an element in the row. The function should return an error message if the input is not a valid 3x3 matrix.
"""

def transpose_matrix(matrix):
    """
    Returns the mathematical transpose of a 3x3 bi-dimensional matrix.
    
    Args:
    matrix (list): A 3x3 bi-dimensional matrix represented as a list of lists.
    
    Returns:
    list: The transpose of the input matrix, or an error message if the input is not a valid 3x3 matrix.
    """
    
    # Validate the input first
    if type(matrix) is not list or len(matrix) != 3:
        return "Invalid input: Not a matrix"
    for row in matrix:
        if type(row) is not list or len(row) != 3:
            return "Invalid input: Not a 3x3 matrix"
    
    # If the input is valid, get the transpose
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed