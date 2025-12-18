"""
QUESTION:
Create a function called `transpose_matrix(matrix)` that takes a square matrix as input and returns its transpose. The input matrix will have the same number of rows and columns (1-10), and its elements will be integers or floats within the range of [-100, 100]. The solution should have a time complexity of O(N^2) and a space complexity of O(N^2), where N is the number of rows/columns in the matrix.
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