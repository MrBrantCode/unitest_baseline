"""
QUESTION:
Write a function `num_of_routes(n, m)` that calculates the distinct permutations of traversing pathways to reach the top right corner from the lower left corner in an n x m matrix, where movement is restricted to upward or rightward directions. The function should return the total number of distinct pathways.
"""

def num_of_routes(n, m):
    matrix = [[0 for x in range(m)] for x in range(n)]
    
    for i in range(n):
        matrix[i][0] = 1

    for i in range(m):
        matrix[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[n-1][m-1]