"""
QUESTION:
You are given an `n x n` grid where each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of cell `(i, j)`. The value `-1` in the grid represents an obstacle. Return the total surface area of the resulting shapes after placing these cubes and gluing any directly adjacent cubes to each other. 

The surface area of the obstacles is not counted, and the bottom face of each shape counts toward its surface area. The function should be named `surfaceArea` and it should take a 2D array `grid` as input. The constraints are `1 <= n <= 50` and `-1 <= grid[i][j] <= 50`.
"""

def surfaceArea(grid):
    n = len(grid)
    area = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] < 0: continue
            area += 2  # for top and bottom surface of cube
            # for four sides
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                # if there's an obstacle or edge, add all height to area
                if nx < 0 or ny < 0 or nx == n or ny == n or grid[nx][ny] < 0:
                    area += grid[i][j]
                else:
                    area += max(grid[i][j] - grid[nx][ny], 0)
    return area