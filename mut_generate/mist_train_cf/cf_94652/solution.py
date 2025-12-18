"""
QUESTION:
Write a function named `find_largest_number` that takes a 2D list `matrix` as input. The function should return a tuple containing the largest number in the matrix and a list of its coordinates (row and column). If the matrix is empty, the function should raise a custom exception named `EmptyMatrixException` with the error message "Matrix is empty." If there are multiple occurrences of the largest number, the function should return the coordinates of all occurrences. The matrix can contain both positive and negative numbers.
"""

class EmptyMatrixException(Exception):
    pass

def find_largest_number(matrix):
    if not matrix:
        raise EmptyMatrixException("Matrix is empty.")
    
    largest_number = float('-inf')
    largest_number_coordinates = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > largest_number:
                largest_number = matrix[row][col]
                largest_number_coordinates = [(row, col)]
            elif matrix[row][col] == largest_number:
                largest_number_coordinates.append((row, col))

    return largest_number, largest_number_coordinates