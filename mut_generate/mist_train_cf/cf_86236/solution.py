"""
QUESTION:
Write a function named `calculate_transpose` that takes a matrix as input, calculates its transpose, and checks if the matrix is symmetric. The function should return a tuple containing a boolean value indicating whether the matrix is symmetric and the transposed matrix. The input matrix will be a list of lists of integers with a value range of -1000 to 1000. The time complexity and space complexity of the function should be O(mn), where m is the number of rows and n is the number of columns in the matrix.
"""

def calculate_transpose(matrix):
    # Get the number of rows and columns
    m = len(matrix)
    n = len(matrix[0])
    
    # Create a new matrix with n rows and m columns
    transpose = [[0 for _ in range(m)] for _ in range(n)]
    
    # Calculate the transpose by swapping rows with columns
    for i in range(m):
        for j in range(n):
            transpose[j][i] = matrix[i][j]
    
    # Check if the matrix is symmetric
    symmetric = matrix == transpose
    
    return symmetric, transpose