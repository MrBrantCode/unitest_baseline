"""
QUESTION:
Create a function called transpose_matrix(matrix) that takes a square matrix (number of rows = number of columns) as input, where the elements can be integers or floats within the range of [-100, 100], and returns its transpose by swapping its rows with columns. The size of the matrix can range from 1x1 to 10x10, and the time and space complexities should be O(N^2), where N is the number of rows/columns in the matrix.
"""

def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    
    # Create an empty result matrix
    result = [[0 for _ in range(rows)] for _ in range(columns)]
    
    # Transpose the matrix
    for i in range(columns):
        for j in range(rows):
            result[i][j] = matrix[j][i]
    
    return result