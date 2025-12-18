"""
QUESTION:
Create a function named construct_matrix that constructs a matrix with a specified number of rows and columns. The function should take two parameters, rows and cols, representing the number of rows and columns in the matrix. The function should return a 2D list filled with zeros, where the length of the outer list represents the number of rows and the length of each inner list represents the number of columns.
"""

def construct_matrix(rows, cols):
    """
    Construct a matrix with a specified number of rows and columns filled with zeros.
    
    Args:
    rows (int): The number of rows in the matrix.
    cols (int): The number of columns in the matrix.
    
    Returns:
    list: A 2D list filled with zeros, where the length of the outer list represents the number of rows and the length of each inner list represents the number of columns.
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]