"""
QUESTION:
Create a function named `print_matrices` that takes an integer parameter `n` and returns two square matrices of dimension nxn. The first matrix should contain successive positive integers from 1 to n^2 in row-major order, and the second matrix should contain the same integers in column-major order. The function must validate the input, ensuring `n` is a positive integer not greater than 10. If the input is invalid, return an error message instead of the matrices.
"""

def print_matrices(n):
    # Validate the input
    if type(n) != int or n <= 0 or n > 10:
        return "Error: Invalid input! Please enter a positive integer not greater than 10."

    # Initialize the matrices
    row_major = [[0]*n for _ in range(n)]
    col_major = [[0]*n for _ in range(n)]

    # Fill in the row-major matrix
    num = 1
    for i in range(n):
        for j in range(n):
            row_major[i][j] = num
            num += 1

    # Fill in the column-major matrix
    num = 1
    for j in range(n):
        for i in range(n):
            col_major[i][j] = num
            num += 1

    return row_major, col_major