"""
QUESTION:
Write a function named `sum_and_transpose(matrix1, matrix2)` that takes two 2D matrices as input. The function should return the transpose of the sum of the two input matrices if they have the same dimensions; otherwise, return an error message "Error: matrices are of different dimensions!".
"""

def sum_and_transpose(matrix1, matrix2):
    # Check if the dimensions of the two matrices are equal
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Error: matrices are of different dimensions!"

    # Initialize an empty matrix for the sum
    sum_matrix = [[0 for row in range(len(matrix1[0]))] for col in range(len(matrix1))]

    # Sum the matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    # Transpose the sum matrix
    transpose_matrix = [[0 for row in range(len(sum_matrix))] for col in range(len(sum_matrix[0]))]
    for i in range(len(sum_matrix)):
        for j in range(len(sum_matrix[0])):
            transpose_matrix[j][i] = sum_matrix[i][j]

    return transpose_matrix