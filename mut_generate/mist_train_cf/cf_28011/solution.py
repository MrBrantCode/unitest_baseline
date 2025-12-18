"""
QUESTION:
Implement the `calculate_determinant` function, which takes a square matrix as input, represented as a list of lists where each inner list represents a row of the matrix. The function should return the determinant of the given matrix. The matrix will have at least 1 row and 1 column, and all rows will have the same number of elements as the number of rows.
"""

def calculate_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            minor = [row[:i] + row[i+1:] for row in matrix[1:]]
            det += ((-1) ** i) * matrix[0][i] * calculate_determinant(minor)
        return det