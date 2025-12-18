"""
QUESTION:
Write a function `transpose_matrix(matrix)` that takes a 2D matrix as input and returns its transpose. The function should replace non-numeric elements with the character "-". The dimensions of the input matrix are m x n, where m and n are positive integers, and the output matrix should have dimensions n x m with the rows and columns of the input matrix swapped.
"""

def transpose_matrix(matrix):
    # Get the dimensions of the input matrix
    m = len(matrix)
    n = len(matrix[0])
    
    # Create a new matrix with dimensions n x m
    new_matrix = [[None for i in range(m)] for j in range(n)]
    
    # Iterate over the input matrix and swap rows with columns
    for i in range(m):
        for j in range(n):
            # If the element is non-numeric, replace it with the special character "-"
            if not isinstance(matrix[i][j], (int, float)):
                new_matrix[j][i] = "-"
            else:
                new_matrix[j][i] = matrix[i][j]
    
    return new_matrix