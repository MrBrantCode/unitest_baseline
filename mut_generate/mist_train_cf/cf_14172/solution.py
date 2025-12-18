"""
QUESTION:
Write a function `calculate_sum(matrix)` that takes a 2D list of integers as input, calculates the sum of each row and each column, and returns the row sums and column sums as two separate lists. The time complexity of the solution should be O(n * m) and the space complexity should be O(n + m), where n is the number of rows and m is the number of columns in the matrix.
"""

def calculate_sums(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    row_sums = [0] * num_rows
    col_sums = [0] * num_cols

    for i in range(num_rows):
        for j in range(num_cols):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]

    return row_sums, col_sums