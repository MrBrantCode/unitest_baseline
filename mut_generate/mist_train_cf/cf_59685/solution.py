"""
QUESTION:
Given a grid with the following rules: 
- 0 is an empty cell
- 1 is the starting cell
- 2 is the ending cell
- -1 is an obstacle
Implement a function `uniquePathsIII` that returns the number of unique paths from the start to the end cell, given the restriction that you can only move in four directions (up, down, left, right).
"""

def uniquePathsIII(grid):
    m, n = len(grid), len(grid[0])
    ans, empties, x, y, dx, dy = 0, 0, 0, 0, [-1, 0, 1, 0], [0, 1, 0, -1]
    
    def dfs(x, y, empties):
        nonlocal ans
        if not (0 <= x < m and 0 <= y < n) or grid[x][y] < 0:
            return
        elif grid[x][y] == 2:
            ans += empties == 0
        else:
            temp, grid[x][y] = grid[x][y], -2
            for k in range(4):
                dfs(x + dx[k] , y + dy[k], empties - (temp == 0))
            grid[x][y] = temp

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                x, y = (i, j)
            elif grid[i][j] == 0:
                empties += 1
            elif grid[i][j] == 2:
                empties -= 1

    dfs(x, y, empties)
    return ans