"""
QUESTION:
Create a function called `transpose_matrix(matrix)` that takes a square matrix as input and returns its transpose. The input matrix will have between 1 and 10 rows (and an equal number of columns), with integer or float elements within the range [-100, 100].
"""

def transpose_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    columns = len(matrix[0])
    
    # Initialize an empty result matrix
    result = [[0] * rows for _ in range(columns)]
    
    # Transpose the matrix
    for i in range(columns):
        for j in range(rows):
            result[i][j] = matrix[j][i]
    
    return result