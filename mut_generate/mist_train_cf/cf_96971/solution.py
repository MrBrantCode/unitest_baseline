"""
QUESTION:
Write a function `find_determinant(matrix)` to calculate the determinant of a square matrix represented as a list of lists. The function should take a 2D list `matrix` as input, where each inner list represents a row of the matrix, and return the determinant of the matrix. The input matrix is guaranteed to be a square matrix of size n x n.
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