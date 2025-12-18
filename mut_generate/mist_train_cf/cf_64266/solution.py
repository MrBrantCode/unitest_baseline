"""
QUESTION:
Given a grid of 0s and 1s, find the number of corner rectangles with distinct 1s as corners and all 1s on the diagonals. The grid will have between 1 and 200 rows and columns, and each cell will be either 0 or 1. There will be at most 6000 1s in the grid. The function should return the count of such rectangles.

Implement a function named `countCornerRectangles` that takes a 2D list `grid` as input and returns the count of corner rectangles satisfying the conditions.
"""

def countCornerRectangles(grid):
    m, n = len(grid), len(grid[0]) if grid else 0
    dp, ans = [[0]*n for _ in range(n)], 0
    def isValid(i, j1, j2):
        for j in range(j1, j2+1):
            if grid[i][j] == 0:
                return False
        return True
    for i in range(m):
        for j1 in range(n):
            if grid[i][j1]:
                for j2 in range(j1+1, n):
                    if grid[i][j2] and isValid(i, j1, j2):
                        ans += dp[j1][j2]
                        dp[j1][j2] += 1
    return ans