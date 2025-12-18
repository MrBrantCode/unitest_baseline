"""
QUESTION:
Write a function named `transpose_matrix` that takes a 2D list `matrix` as input, calculates its transpose, and returns the result. The function should have a time complexity of O(mn) and a space complexity of O(mn), where m and n are the number of rows and columns in the matrix, respectively. The transpose of a matrix is obtained by swapping its rows with columns, i.e., the element at position [i][j] in the original matrix should be at position [j][i] in the transposed matrix.
"""

def transpose_matrix(matrix):
    # Get the number of rows and columns in the matrix
    m = len(matrix)
    n = len(matrix[0])
    
    # Create a new matrix with dimensions n x m
    transpose = [[0] * m for _ in range(n)]
    
    # Populate the transpose matrix
    for i in range(m):
        for j in range(n):
            transpose[j][i] = matrix[i][j]
    
    return transpose