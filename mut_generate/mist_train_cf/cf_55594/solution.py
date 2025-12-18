"""
QUESTION:
Write a function `longestIncreasingPath(matrix)` that takes a matrix of integers and returns the length of the longest increasing path in the matrix. 

The function should find all cells in the matrix with a value of 2 and start a depth-first search (DFS) from these cells, considering four possible directions (up, down, left, right) for each cell. If the adjacent cell has a larger value than the current cell, continue the DFS from the adjacent cell. The function should use memoization to store the longest increasing path lengths for each cell to avoid repeated calculations.

The function should return the maximum length of the longest increasing paths found. If the input matrix is empty or has no cells with a value of 2, the function should return 0.
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
        lookup[i][j] = longest + 1 
        return lookup[i][j]

    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    max_len = 0
    lookup = [[-1]*n for _ in range(m)]
    checkpoints = ((i, j) for i in range(m) for j in range(n) if matrix[i][j]==2)
    for chk in checkpoints:
        max_len = max(max_len, dfs(*chk))
    return max_len