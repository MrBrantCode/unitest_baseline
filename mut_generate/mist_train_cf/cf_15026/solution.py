"""
QUESTION:
Create a function called `transpose_matrix(matrix)` that takes a square matrix as input and returns its transpose. The input matrix will always be a square matrix (number of rows = number of columns), contain elements that are integers or floats within the range of [-100, 100], and have a size ranging from 1x1 to 10x10.
"""

def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    result = [[0] * rows for _ in range(columns)]
    for i in range(columns):
        for j in range(rows):
            result[i][j] = matrix[j][i]
    return result