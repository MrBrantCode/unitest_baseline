"""
QUESTION:
You are given a 2D grid consisting of 0s (water) and 1s (land). The function `largestIsland(grid)` should return the area of the largest possible island if you can change one water cell to land. The grid is non-empty and contains at least one 0 and one 1. The length and width of the grid are the same.
"""

def largestIsland(grid):
    n = len(grid)
    directions = [(0,1),(0,-1),(-1,0),(1,0)]
    id = 2
    id_to_size = {0: 0}

    def dfs(x, y, id):
        size = 1
        grid[x][y] = id
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                size += dfs(nx, ny, id)
        return size

    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                id_to_size[id] = dfs(x, y, id)
                id += 1

    max_area = max(id_to_size.values())

    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                seen = {grid[nx][ny] for dx,dy in directions for nx,ny in [(x+dx, y+dy)] if 0<=nx<n and 0<=ny<n}
                max_area = max(max_area, 1 + sum(id_to_size[i] for i in seen))
    return max_area