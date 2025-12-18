"""
QUESTION:
Create a function `max1EnclosedSquare(grid)` that takes a 2D matrix `grid` of binary digits (0s and 1s) and returns the total number of elements in the largest square submatrix that is entirely enclosed by 1s on its periphery, or returns 0 if no such submatrix can be found within the grid. The length of grid is within the range 1 <= grid.length <= 100 and the length of grid[0] is within the range 1 <= grid[0].length <= 100.
"""

def max1EnclosedSquare(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    maxSide = 0
    
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = grid[i][j]
            elif grid[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
            maxSide = max(maxSide, dp[i][j])
            
    return maxSide * maxSide