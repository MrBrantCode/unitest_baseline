"""
QUESTION:
Write a function `reachablePaths(m, n)` that calculates the number of routes from the top-left corner to the bottom-right corner in an `m x n` grid, where movements can be to the right, down, or diagonally (bottom-right).
"""

def reachablePaths(m, n):
    grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i==m and j==n:
                grid[i][j] = 1
            else:
                right = 0 if j==n else grid[i][j+1]
                down = 0 if i==m else grid[i+1][j]
                diagonal = 0 if i==m or j==n else grid[i+1][j+1]
                grid[i][j] = right + down + diagonal
    return grid[0][0]