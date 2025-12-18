"""
QUESTION:
Write a function called `reverse_matrix` that takes a 2D list of numbers as input, where the number of rows and columns are at least 2, and can be different (i.e., the matrix is not necessarily square). The function should return a new matrix where the order of both rows and columns are reversed.
"""

def reverse_matrix(matrix):
    """
    This function takes a 2D list of numbers as input and returns a new matrix 
    where the order of both rows and columns are reversed.

    Args:
        matrix (list): A 2D list of numbers.

    Returns:
        list: A new matrix with reversed rows and columns.
    """
    return [row[::-1] for row in matrix[::-1]]