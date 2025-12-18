"""
QUESTION:
Write a function `max_in_matrix(matrix)` that finds the largest numerical component within a 2D matrix dataset. The matrix is a list of lists where each element is an integer between -10^3 and 10^3, and the matrix size is at most 50x50.
"""

def max_in_matrix(matrix):
    max_val = matrix[0][0]  # Initialize max_val with the first element of the matrix
    for row in matrix:
        for num in row:
            if num > max_val:
                max_val = num  # Update max_val if the current number is greater
    return max_val