"""
ORIGINAL QUESTION:
Write a function `findMaxPath` that takes a 2D array as input and returns the maximum path sum. The path can start and end at any point of the grid and can only move either downwards or rightwards at any point of time, without visiting the same cell more than once.
"""

def findMaxPath(mat):
    rows = len(mat)
    cols = len(mat[0])
    
    dp = [[0]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            dp[i][j] = mat[i][j]
            
    for i in range(1, rows):
        for j in range(cols):
            if j > 0:
                dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] += dp[i - 1][j]
                
    for j in range(1, cols):
        for i in range(rows):
            if i > 0:
                dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] += dp[i][j - 1]
                
    max_sum = float('-inf')
    for i in range(rows):
        for j in range(cols):
            max_sum = max(max_sum, dp[i][j])
            
    return max_sum