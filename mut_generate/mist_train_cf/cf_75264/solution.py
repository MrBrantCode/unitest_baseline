"""
QUESTION:
Write a function named `max_area` that takes a 2D matrix of integers (0s and 1s) as input and returns the coordinates of the top-left and bottom-right corners of the largest square sub-matrix composed of only '1s'. The function should return the coordinates as tuples (i, j) where i and j are 0-indexed. If multiple such sub-matrices with maximum area exist, the function can return any one. The input matrix will be non-empty and contain only '0's and '1's.
"""

def max_area(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Initialization
    sizes = [[0]*(num_cols+1) for _ in range(num_rows+1)]
    max_size = 0
    max_i, max_j = 0, 0

    # Update sizes
    for i in range(1, num_rows+1):
        for j in range(1, num_cols+1):
            if matrix[i-1][j-1] == '1':
                sizes[i][j] = min(sizes[i][j-1], sizes[i-1][j], sizes[i-1][j-1]) + 1
                if sizes[i][j] > max_size:
                    max_size = sizes[i][j]
                    max_i, max_j = i-1, j-1

    return (("Top left", (max_i - max_size + 1, max_j - max_size + 1)), ("Bottom right", (max_i, max_j)))