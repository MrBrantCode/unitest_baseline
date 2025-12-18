"""
QUESTION:
Implement a function `is_matrix_palindrome(matrix)` that determines whether a given matrix of integers is a numeric palindrome. A numeric palindrome is a matrix that reads the same backward as forward, considering both row-wise and column-wise sequences. The function should return a boolean value indicating whether the matrix is a palindrome or not.
"""

def entrance(matrix):
    # Calculate the transpose of matrix
    transpose_matrix = list(map(list, zip(*matrix)))

    for row in matrix:
        # Check if row is not a palindrome
        if row != row[::-1]:
            return False
    
    for row in transpose_matrix:
        # Check if column (row in transpose_matrix) is not a palindrome
        if row != row[::-1]:
            return False

    return True