"""
QUESTION:
Implement a function `maxProductPath` to find the maximum product of a path from the top left to the bottom right of a given grid. The function should take a 2D grid as input and return the maximum product of the path as an integer. The product is taken modulo 10^9 + 7 to prevent overflow. If the maximum product is negative, return -1.
"""

def maxProductPath(grid):
    MOD = 10**9 + 7
    rows, cols = len(grid), len(grid[0])
    dp = [[None]*cols for _ in range(rows)]
    dp[0][0] = (grid[0][0], grid[0][0])  # maxProd, minProd

    # populate first row
    for j in range(1, cols):
        dp[0][j] = (dp[0][j-1][0]*grid[0][j] % MOD, dp[0][j-1][1]*grid[0][j] % MOD)

    # populate first column
    for i in range(1, rows):
        dp[i][0] = (dp[i-1][0][0]*grid[i][0] % MOD, dp[i-1][0][1]*grid[i][0] % MOD)

    # populate rest of the dp array
    for i in range(1, rows):
        for j in range(1, cols):
            nums = [dp[i-1][j][0]*grid[i][j], dp[i-1][j][1]*grid[i][j],
                    dp[i][j-1][0]*grid[i][j], dp[i][j-1][1]*grid[i][j]]
            dp[i][j] = (max(nums) % MOD, min(nums) % MOD)

    maxVal = dp[-1][-1][0]
    return maxVal if maxVal >= 0 else -1