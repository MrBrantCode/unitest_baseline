"""
QUESTION:
Write a function `calculateTrappedWater(grid)` that takes in a 2D grid of non-negative integers representing the height of the terrain at each location and returns the total water trapped within the grid. The function should calculate the total water trapped by comparing each cell's height with its neighboring cells and accumulating the differences. The grid can be of any size, but it must be rectangular (i.e., all rows have the same number of columns).
"""

def calculateTrappedWater(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    left_max = [[0] * n for _ in range(m)]
    right_max = [[0] * n for _ in range(m)]
    top_max = [[0] * n for _ in range(m)]
    bottom_max = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            left_max[i][j] = max(left_max[i][j - 1], grid[i][j]) if j > 0 else grid[i][j]
            top_max[i][j] = max(top_max[i - 1][j], grid[i][j]) if i > 0 else grid[i][j]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            right_max[i][j] = max(right_max[i][j + 1], grid[i][j]) if j < n - 1 else grid[i][j]
            bottom_max[i][j] = max(bottom_max[i + 1][j], grid[i][j]) if i < m - 1 else grid[i][j]

    total_water = 0
    for i in range(m):
        for j in range(n):
            water_level = min(left_max[i][j], right_max[i][j], top_max[i][j], bottom_max[i][j])
            total_water += max(0, water_level - grid[i][j])

    return total_water