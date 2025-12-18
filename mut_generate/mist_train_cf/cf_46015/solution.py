"""
QUESTION:
Implement a function `uniquePathsIII(grid)` that takes a 2D grid as input and returns the number of 4-directional walks from the starting square (`1`) to the ending square (`2`) that walk over every non-obstacle square (`0`) exactly once and the special square (`3`) exactly twice. The starting and ending square can be anywhere in the grid. The grid size is bounded by 1 <= grid.length * grid[0].length <= 25.
"""

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
def uniquePathsIII(grid):
    def dfs(x, y, empties):
        nonlocal ans
        if not (0 <= x < m and 0 <= y < n) or grid[x][y] < 0:
            return
        elif grid[x][y] == 2:
            ans += empties == 0
        else:
            grid[x][y] = -2
            for k in range(4):
                dfs(x + dx[k], y + dy[k], empties - 1)
            grid[x][y] = 0

    m, n, ans, empties = len(grid), len(grid[0]), 0, 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                x, y = (i, j)
            elif grid[i][j] == 0:
                empties += 1
            elif grid[i][j] == 3:
                empties += 2

    dfs(x, y, empties)
    return ans