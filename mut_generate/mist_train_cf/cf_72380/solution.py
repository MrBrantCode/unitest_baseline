"""
QUESTION:
Write a function `findPaths(m, n, N, i, j, x, y, grid)` that calculates the number of paths to move a ball from a start position `(i, j)` to a target position `(x, y)` within a grid of size `m x n` with obstacles, where the ball can move at most `N` times in four directions (up, down, left, right) and the path cannot pass through obstacles. The grid is represented by a 2D array where 0 represents an open cell, 1 represents an obstacle, and 2 represents the target. The function should return the number of paths modulo 10^9 + 7. The length and height of the grid are in range [1,50] and N is in range [0,50].
"""

def findPaths(m, n, N, i, j, x, y, grid):
    MOD = 10**9 + 7
    dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N+1)]
    dp[0][i][j] = 1
    for moves in range(1, N+1):
        for X in range(m):
            for Y in range(n):
                if grid[X][Y] != 1:  
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = X + dx, Y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            dp[moves][X][Y] += dp[moves-1][nx][ny]
                            dp[moves][X][Y] %= MOD
    return dp[N][x][y]