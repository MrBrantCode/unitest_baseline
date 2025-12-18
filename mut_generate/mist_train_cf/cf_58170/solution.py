"""
QUESTION:
Create a function called `largestIsland` that takes a binary matrix `grid` of dimensions `n x n` as input, where `n` ranges from 1 to 500 and `grid[i][j]` can only be `0` or `1`. The function should return the maximum possible size of an island in the `grid` after modifying a single `0` to `1`, where an island is defined as a cluster of `1`s connected in all four directions.
"""

def largestIsland(grid):
    n = len(grid)
    directions = ((0,1),(0,-1),(-1,0),(1,0))
    id = 2
    id_to_size = {0: 0}
    
    def dfs(x, y, id):
        size = 1
        grid[x][y] = id
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx>=0 and nx<n and ny>=0 and ny<n and grid[nx][ny] == 1:
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