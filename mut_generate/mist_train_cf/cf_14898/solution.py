"""
QUESTION:
Write a function `find_max_sum_path(matrix)` that finds a path from the top-left corner to the bottom-right corner of a given 2D matrix that maximizes the sum of numbers. The function should allow movement in three directions: right, down, or diagonally right-down. The function should return the maximum sum path.

The input matrix is a 2D list of integers. The function should not have any other inputs or outputs. The function should not assume any specific size or values for the input matrix.
"""

def find_max_sum_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the maximum sum values
    max_sum_matrix = [[0] * cols for _ in range(rows)]

    # Initialize the first row and first column of the new matrix
    max_sum_matrix[0] = matrix[0]
    for i in range(1, rows):
        max_sum_matrix[i][0] = max_sum_matrix[i-1][0] + matrix[i][0]

    # Calculate the maximum sum values for each position in the new matrix
    for i in range(1, rows):
        for j in range(1, cols):
            max_sum_matrix[i][j] = max(max_sum_matrix[i-1][j], max_sum_matrix[i][j-1], max_sum_matrix[i-1][j-1]) + matrix[i][j]

    # Find the maximum sum path
    max_sum_path = []
    i = rows - 1
    j = cols - 1
    max_sum_path.append(matrix[i][j])

    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if max_sum_matrix[i-1][j] >= max_sum_matrix[i][j-1] and max_sum_matrix[i-1][j] >= max_sum_matrix[i-1][j-1]:
                i -= 1
            elif max_sum_matrix[i][j-1] >= max_sum_matrix[i-1][j] and max_sum_matrix[i][j-1] >= max_sum_matrix[i-1][j-1]:
                j -= 1
            else:
                i -= 1
                j -= 1
        max_sum_path.insert(0, matrix[i][j])

    return sum(max_sum_path)