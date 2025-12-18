"""
QUESTION:
Create a function named `calculate_determinant` that takes a 3x3 matrix as input and returns its determinant using Sarrus' rule. The input matrix should be a list of lists, where each inner list represents a row of the matrix. The function should calculate the determinant by summing the products of the main diagonals and subtracting the sum of the products of the anti-diagonals.
"""

def calculate_determinant(matrix):
    main_diag = matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[0][1]*matrix[1][2]*matrix[2][0] + matrix[0][2]*matrix[1][0]*matrix[2][1]
    anti_diag = matrix[2][0]*matrix[1][1]*matrix[0][2] + matrix[1][0]*matrix[0][1]*matrix[2][2] + matrix[0][0]*matrix[1][2]*matrix[2][1]
    det = main_diag - anti_diag
    return det