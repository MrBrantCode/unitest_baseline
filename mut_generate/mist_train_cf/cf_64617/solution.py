"""
QUESTION:
Write a function `minimal_submatrix(matrix, target)` that takes a 2D list `matrix` and a numerical `target` as input and returns the smallest submatrix where the sum of its elements equals the `target` value. The function should return the smallest possible submatrix in terms of the total number of elements. If multiple submatrices have the same minimum size, return any of them.
"""

def minimal_submatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    min_size = m * n + 1  
    min_submatrix = None  

    prefix_sum = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j] + matrix[i][j]

    for i in range(m):
        for j in range(n):
            for k in range(i+1, m+1):
                for l in range(j+1, n+1):
                    if prefix_sum[k][l] - prefix_sum[i][l] - prefix_sum[k][j] + prefix_sum[i][j] == target:
                        size = (k-i) * (l-j)
                        if size < min_size:
                            min_size = size
                            min_submatrix = [[matrix[x][y] for y in range(j, l)] for x in range(i, k)]

    return min_submatrix