"""
QUESTION:
Write a function named `transpose` that takes a 2D list (matrix) as input and returns its transpose. The function should swap the rows and columns of the input matrix and return the resulting matrix. The input matrix is a list of lists, where each inner list has the same length, and the function should work for any size of matrix.
"""

def transpose(matrix):
    # Get the dimensions of the original matrix
    m = len(matrix)
    n = len(matrix[0])
    
    # Initialize the result matrix
    result = [[0 for _ in range(m)] for _ in range(n)]
    
    # Iterate through each element of the original matrix
    for i in range(m):
        for j in range(n):
            # Swap the row index with the column index
            result[j][i] = matrix[i][j]
    
    # Return the transposed matrix
    return result