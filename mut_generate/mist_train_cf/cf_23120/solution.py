"""
QUESTION:
Write a function named `print_spiral(matrix)` that takes a 2D list `matrix` as input and returns a list representing the spiral ordering of the input matrix. The input matrix can be of any size and may contain any type of elements. The function should return the elements in the order they would be visited in a clockwise spiral traversal of the matrix, starting from the top left corner.
"""

def print_spiral(matrix):
    """
    This function takes a 2D list (matrix) as input and returns a list representing 
    the spiral ordering of the input matrix.

    Args:
        matrix (list): A 2D list of elements.

    Returns:
        list: A list of elements in spiral order.
    """
    result = []
    while matrix:
        # append the first row
        result += matrix.pop(0)
        # rotate the matrix clockwise
        matrix = (list(zip(*matrix)))[::-1]  # Transpose and reverse each row
    return result