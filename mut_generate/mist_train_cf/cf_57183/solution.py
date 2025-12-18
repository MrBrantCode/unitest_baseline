"""
QUESTION:
Write a function `containsCycle` that takes a 2D array of characters `grid` as input and returns `True` if there exists any cycle consisting of the same value in `grid`, otherwise returns `False`. A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. You can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell. You cannot move to the cell that you visited in your last move.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 500`
- `1 <= n <= 500`
- `grid` consists only of lowercase English letters.
"""

def containsCycle(grid):
    n, m = len(grid), len(grid[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def visit(i, j, x, y, vis):
        vis[i][j] = True
        for k in range(4):
            ni, nj = i+dx[k], j+dy[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or (ni == x and nj == y) or grid[ni][nj] != grid[i][j]:
                continue
            if vis[ni][nj]:
                return True
            if visit(ni, nj, i, j, vis):
                return True
        return False

    vis = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and visit(i, j, -1, -1, vis):
                return True
    return False