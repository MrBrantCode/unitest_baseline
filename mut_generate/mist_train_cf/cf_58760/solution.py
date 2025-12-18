"""
QUESTION:
Write a function `longestIncreasingPath(matrix)` that takes a 2D array of integers as input and returns the length of the longest increasing subsequence in the array. The subsequence can be contiguous and traverse in any direction (horizontal, vertical, or diagonal). The function should use dynamic programming and memoization for efficiency. The array can be empty, and the function should handle this case by returning 0.
"""

def longestIncreasingPath(matrix):
    if not matrix: return 0
    directions=[(-1, 0), (1, 0), (0, -1), (0, 1), (1,1), (-1,-1), (-1,1), (1,-1)]
    m, n = len(matrix), len(matrix[0])
    cache = [[-1]*n for _ in range(m)]

    def dfs(i, j):
        if cache[i][j] != -1:
            return cache[i][j]
        val = matrix[i][j]
        cache[i][j] = 1+max(
            (dfs(i+di, j+dj) for di, dj in directions if 0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj] > val),
            default=0)
        return cache[i][j]

    return max(dfs(x, y) for x in range(m) for y in range(n))