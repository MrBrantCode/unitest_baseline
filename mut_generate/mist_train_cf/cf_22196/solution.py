"""
QUESTION:
Write a function `find_determinant(matrix)` that calculates the determinant of a given square matrix. The matrix is represented as a list of lists, where each inner list represents a row of the matrix. The function should be able to handle square matrices of any size and return the determinant as a result. The input matrix is guaranteed to be square.
"""

def find_determinant(matrix):
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(n):
            sub_matrix = [row[:] for row in matrix]
            sub_matrix.pop(0)
            for j in range(n - 1):
                sub_matrix[j].pop(i)
            if i % 2 == 0:
                determinant += matrix[0][i] * find_determinant(sub_matrix)
            else:
                determinant -= matrix[0][i] * find_determinant(sub_matrix)
        return determinant