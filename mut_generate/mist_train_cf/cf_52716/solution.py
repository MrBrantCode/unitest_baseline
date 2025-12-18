"""
QUESTION:
Write a function called `determinant(matrix)` that calculates the determinant of a given square matrix using Laplace expansion. The matrix is represented as a 2D list of integers, and the function should return the determinant value.
"""

def determinant(matrix):
    #Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        #Construct a sub-matrix
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        sign = -1 if c % 2 else 1  # alternate signs for each cofactor
        sub_det = determinant(sub_matrix) #recursively calculate determinant
        det += sign * matrix[0][c] * sub_det
    return det