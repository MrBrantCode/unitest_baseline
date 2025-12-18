"""
QUESTION:
Given a matrix of m x n integers, find the length of the longest increasing path in the matrix where -1 represents an obstacle and -2 represents a checkpoint. From each cell, you can move in four directions: left, right, up, or down. You must pass through all checkpoints to complete the path and the path can start and end at any cell. 

The function should be named longestIncreasingPath and it takes a 2D list of integers as input. The constraints are 1 <= m, n <= 200 and -2 <= matrix[i][j] <= 231 - 1.
"""

def longestIncreasingPath(matrix):
    def dfs(i, j):
        if lookup[i][j] != -1:
            return lookup[i][j]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        longest = 0
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                longest = max(longest, dfs(x, y))
        lookup[i][j] = longest + 1  # update the lookup table
        return lookup[i][j]

    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    lookup = [[-1]*n for _ in range(m)]
    checkpoints = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == -2]
    return max(dfs(*chk) for chk in checkpoints) if checkpoints else 0