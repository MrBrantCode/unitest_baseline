"""
QUESTION:
Write a function `transpose(matrix)` that takes a 2D matrix as input and returns its transpose. The function should be able to handle matrices with up to 1000 rows and 1000 columns, and the values in the matrix can be integers ranging from -10^9 to 10^9.
"""

def transpose(matrix):
    m = len(matrix) 
    n = len(matrix[0]) 

    # Initialize result matrix
    transposed_matrix = [[0 for _ in range(m)] for _ in range(n)]

    # Transpose the matrix
    for i in range(m):
        for j in range(n):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix