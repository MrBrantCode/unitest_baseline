"""
QUESTION:
Write a function `find_determinant(matrix)` that calculates the determinant of a square matrix represented as a list of lists, where each inner list represents a row of the matrix. The function should take a 2D list as input and return the determinant of the matrix.
"""

def find_determinant(matrix):
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(n):
            sub_matrix = [row[:] for row in matrix[1:]]
            for j in range(n - 1):
                sub_matrix[j].pop(i)
            determinant += ((-1) ** i) * matrix[0][i] * find_determinant(sub_matrix)
        return determinant