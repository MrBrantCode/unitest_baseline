"""
QUESTION:
Create a function `is_magic_square(matrix)` that takes a 2D list of integers as input, representing a square matrix. The function should return `True` if the matrix is a magic square and `False` otherwise. A magic square is a square grid filled with distinct positive integers such that each cell contains a different integer and the sum of the integers in each row, each column, or each main diagonal is the same. The input is assumed to be a square matrix (number of rows = number of columns) and this will not be checked by the function.
"""

def is_magic_square(matrix):
    # We convert the matrix into a list of lists for easier manipulation
    matrix = [m[:] for m in matrix]
    
    # Get size of the square
    size = len(matrix)
    
    # Get the magic constant (the sum in each row, column, or diagonal)
    magic_constant = sum(matrix[0])
    
    # Check rows and columns
    for i in range(size):
        if sum(matrix[i]) != magic_constant or sum([row[i] for row in matrix]) != magic_constant:
            return False

    # Check diagonals
    if sum(matrix[i][i] for i in range(size)) != magic_constant or sum(matrix[i][size - i - 1] for i in range(size)) != magic_constant:
        return False

    # If we are here, it means that the matrix is a magic square
    return True