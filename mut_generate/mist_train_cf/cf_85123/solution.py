"""
QUESTION:
Write a function `find_unique_paths(m, n)` that calculates the number of unique paths from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1) in a 2D grid of size m x n, where movements are restricted to either down or right.
"""

def find_unique_paths(m, n):
    # create a 2D table to store results of subproblems
    dp = [[0 for x in range(n)] for y in range(m)]

    # Count of paths to reach any cell in first column is 1
    for i in range(m):
        dp[i][0] = 1

    # Count of paths to reach any cell in first row is 1
    for j in range(n):
        dp[0][j] = 1

    # Fill the dp table in bottom-up manner
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]