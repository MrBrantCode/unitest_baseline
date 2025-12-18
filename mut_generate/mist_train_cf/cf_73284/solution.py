"""
QUESTION:
Write a function `longest_increasing_subsequence(matrix)` to find the length of the longest increasing subsequence in a given 2D list `matrix`. The function should take a 2D list of integers as input and return the length of the longest increasing subsequence. The input matrix is not empty and contains only integers.
"""

def longest_increasing_subsequence(matrix):
    if not matrix: return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[1]*n for _ in range(m)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def dfs(i, j):
        for dx, dy in directions:
            x, y = i+dx, j+dy
            if x<0 or x>=m or y<0 or y>=n or matrix[x][y]<=matrix[i][j]:
                continue
            if not dp[x][y] or dp[x][y] <= dp[i][j]:
                dp[x][y] = dp[i][j] + 1
                dfs(x, y)
    for i in range(m):
        for j in range(n):
            dfs(i, j)
    return max(max(row) for row in dp)