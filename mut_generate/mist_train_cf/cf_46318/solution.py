"""
QUESTION:
Write a function `getMaximumGold` that takes a 2D grid as input, where each cell represents the amount of gold in that cell, and returns the maximum amount of gold that can be collected and the corresponding path in a list, under the following conditions:
- The function can move one step to the left, right, up, or down from the current cell.
- The function cannot visit the same cell more than once.
- The function cannot visit a cell with 0 gold.
- The function can start and stop collecting gold from any position in the grid that has some gold.
- If there are multiple paths with the same amount of gold and the same number of steps, return any of them.

The input grid satisfies the following constraints:
- The number of rows is equal to the number of columns in the grid.
- The number of rows and columns in the grid is between 1 and 15 (inclusive).
- The amount of gold in each cell is between 0 and 100 (inclusive).
- There are at most 25 cells containing gold.
"""

def getMaximumGold(grid):
    maxGold, steps, ans = 0, 0, []
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    
    def dfs(x, y, gold, path):
        nonlocal maxGold, steps, ans
        if gold > maxGold or (gold == maxGold and len(path) < steps):
            maxGold, steps, ans = gold, len(path), path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = True
                dfs(nx, ny, gold + grid[nx][ny], path + [grid[nx][ny]])
                visited[nx][ny] = False
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                visited[i][j] = True
                dfs(i, j, grid[i][j], [grid[i][j]])
                visited[i][j] = False
    
    return maxGold, ans