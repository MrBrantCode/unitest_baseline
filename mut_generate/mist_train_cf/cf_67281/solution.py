"""
QUESTION:
Write a function `minCostPath(matrix)` to find the minimum cost of a path from the top left cell to the bottom right cell of a 2D Matrix and then back to the top right cell. The path can only move rightwards or downwards from the top left cell to the bottom right cell, and then only leftwards or upwards from the bottom right cell to the top right cell. The matrix must be a valid 2D list with at least 2 rows and 2 columns, and can contain negative integers.
"""

def minCostPath(matrix):
    if not isinstance(matrix, list):
        return "Error: Input should be a matrix (2D list)"
    if len(matrix) < 2 or len(matrix[0]) < 2:
        return "Error: Matrix should have at least 2 rows and 2 columns"

    rows = len(matrix)
    cols = len(matrix[0])
    
    # initializing the first value
    matrix[0][0] = matrix[0][0]

    # Initialize first row
    for i in range(1, cols):
        matrix[0][i] += matrix[0][i - 1]

    # Initialize first column
    for i in range(1, rows):
        matrix[i][0] += matrix[i - 1][0]

    for row in range(1, rows):
        for col in range(1, cols):
            matrix[row][col] += min(matrix[row - 1][col], matrix[row][col - 1])

    # retracing path backwards
    reverse_cost = matrix[-1][-1]
    row = rows - 1
    col = cols - 1
    while row != 0 or col != 0:
        if row == 0:
            reverse_cost += matrix[row][col - 1]
            col -= 1
        elif col == 0:
            reverse_cost += matrix[row - 1][col]
            row -= 1
        else:
            if matrix[row - 1][col] < matrix[row][col - 1]:
                reverse_cost += matrix[row - 1][col]
                row -= 1
            else:
                reverse_cost += matrix[row][col - 1]
                col -= 1
    return reverse_cost