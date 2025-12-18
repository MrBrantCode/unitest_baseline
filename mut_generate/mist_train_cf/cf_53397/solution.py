"""
QUESTION:
Write a function `diag_elements(matrix)` that calculates and returns the unique elements of the primary and secondary diagonals of a given square matrix. The function should accept a 2D list `matrix` as input, where the matrix is a square matrix (i.e., the number of rows equals the number of columns). The function should return two sets: one for the unique elements of the primary diagonal and one for the unique elements of the secondary diagonal.
"""

def diag_elements(matrix):
    primary_diag = set()
    secondary_diag = set()
    n = len(matrix)

    for i in range(n):
        primary_diag.add(matrix[i][i])
        secondary_diag.add(matrix[i][n-1-i])

    return primary_diag, secondary_diag