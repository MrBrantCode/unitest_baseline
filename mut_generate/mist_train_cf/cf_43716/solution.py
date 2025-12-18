"""
QUESTION:
Find the number of paths to move a ball out of an m by n grid boundary within N moves. The grid contains obstacles (1) and open cells (0). The ball can move in four directions (up, down, left, right) and cannot move into a cell with an obstacle or move back after crossing the boundary. Return the result modulo 10^9 + 7.

The function `findPaths(m, n, N, i, j, grid)` should take as input the dimensions of the grid (m, n), the maximum number of moves (N), the start coordinate of the ball (i, j), and the grid configuration, and return the number of paths to move the ball out of the grid boundary. The length and height of the grid are in range [1,50] and N is in range [0,50].
"""

def findPaths(m, n, N, i, j, grid):
    MOD = 10**9 + 7
    dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N+1)]
    dp[0][i][j] = 1
    for moves in range(1, N+1):
        for x in range(m):
            for y in range(n):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        dp[moves][nx][ny] += dp[moves-1][x][y]
                        dp[moves][nx][ny] %= MOD
                    elif 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        continue
                    else:
                        dp[moves][x][y] += dp[moves-1][x][y]
                        dp[moves][x][y] %= MOD
    res = 0
    for x in range(m):
        for y in range(n):
            if grid[x][y] == 0:
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    res += dp[N][x][y]
                    res %= MOD
    return res