"""
QUESTION:
Write a function `matrix_dimensions` that takes the number of rows and columns of two matrices A and B as input and returns the dimensions of the product matrix AB if A and B can be multiplied. The function should return an error message if A and B cannot be multiplied. The number of columns in matrix A must be equal to the number of rows in matrix B for the multiplication to be valid.
"""

def matrix_dimensions(rows_A, cols_A, rows_B, cols_B):
    """
    Returns the dimensions of the product matrix AB if A and B can be multiplied.
    
    Args:
        rows_A (int): The number of rows in matrix A.
        cols_A (int): The number of columns in matrix A.
        rows_B (int): The number of rows in matrix B.
        cols_B (int): The number of columns in matrix B.
    
    Returns:
        tuple: A tuple containing the number of rows and columns in the product matrix AB.
        str: An error message if A and B cannot be multiplied.
    """
    if cols_A == rows_B:
        return (rows_A, cols_B)
    else:
        return "Error: Matrices A and B cannot be multiplied."