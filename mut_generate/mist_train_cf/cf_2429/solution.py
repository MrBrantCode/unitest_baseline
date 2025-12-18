"""
QUESTION:
Write a function called `find_largest_number` that takes a matrix as input and returns the largest number in the matrix along with its coordinates. The function should raise a custom exception `EmptyMatrixException` if the matrix is empty. If there are multiple occurrences of the largest number, the function should return the coordinates of all occurrences. The function should have a time complexity of O(m*n), where m and n are the dimensions of the matrix.
"""

class EmptyMatrixException(Exception):
    def __init__(self):
        super().__init__("The matrix is empty.")

def find_largest_number(matrix):
    """
    This function finds the largest number in a matrix and returns it along with its coordinates.

    Args:
    matrix (list): A 2D list representing the matrix.

    Returns:
    tuple: A tuple containing the largest number and its coordinates.

    Raises:
    EmptyMatrixException: If the matrix is empty.
    """
    
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        raise EmptyMatrixException()

    # Initialize the largest number and its coordinates
    largest_number = float('-inf')
    coordinates = []

    # Iterate over the matrix to find the largest number and its coordinates
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > largest_number:
                largest_number = matrix[i][j]
                coordinates = [(i, j)]
            elif matrix[i][j] == largest_number:
                coordinates.append((i, j))

    return largest_number, coordinates