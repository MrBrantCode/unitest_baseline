"""
QUESTION:
Write a function `uniquePathsWithObstacles(obstacleGrid)` that takes a 2D array `obstacleGrid` of size `m x n` where each element is either '0' (free space) or '1' (obstacle) as input, and returns the number of unique paths from the top-left cell to the bottom-right cell of the grid. The robot can only move either down or right at any point in time. The function should assume that `1 <= m, n <= 100` and the top-left and bottom-right cells are always '0'.
"""

def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0]*n for _ in range(m)]

    dp[0][0] = 1 - obstacleGrid[0][0]

    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]