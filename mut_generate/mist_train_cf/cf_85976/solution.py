"""
QUESTION:
Write a function `getMaximumGold` that takes a 2D grid of integers as input and returns a list containing the maximum gold that can be collected and the corresponding path. The grid represents a maze where each cell contains a certain amount of gold, and 0 represents an obstacle. The function should explore all possible paths in the grid using depth-first search (DFS), and return the maximum gold that can be collected along with the path that yields this maximum gold.

The function should start exploring from each cell that contains gold and follow the four directions (up, down, left, and right) until it reaches an obstacle or a cell that has already been visited. The function should keep track of the maximum gold collected so far and the corresponding path, and update these values whenever it finds a path that yields more gold or the same amount of gold with fewer steps.

The input grid is a 2D list of integers, and the function should return a list containing two values: the maximum gold that can be collected and the path that yields this maximum gold.
"""

from typing import List

def getMaximumGold(grid: List[List[int]]) -> List[int]:
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
            if 0<= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = True
                dfs(nx, ny, gold + grid[nx][ny], path + [grid[nx][ny]])
                visited[nx][ny] = False

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                visited[i][j] = True
                dfs(i, j, grid[i][j], [grid[i][j]])
                visited[i][j] = False

    return [maxGold, ans]