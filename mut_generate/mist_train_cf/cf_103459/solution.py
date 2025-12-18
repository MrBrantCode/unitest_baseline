"""
QUESTION:
Write a function named `transpose_matrix` that takes a 2D list of integers, decimals, or characters as input and returns its transpose. The input matrix is guaranteed to have a size of NxM, where 1 <= N, M <= 100, and each element is within the range -1000 to 1000.
"""

def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    # Initialize a new matrix with dimensions MxN
    transpose = [[0] * n for _ in range(m)]
    
    # Iterate over the rows and columns of the original matrix
    for i in range(n):
        for j in range(m):
            # Assign the value of the original matrix to the corresponding position in the transpose matrix
            transpose[j][i] = matrix[i][j]
    
    return transpose