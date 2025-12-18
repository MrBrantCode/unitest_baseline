"""
QUESTION:
Write a function `trapped_water_volume(grid)` that takes a 2D grid of integers as input, where each integer represents the height of a cell in the grid. The function should return the total volume of water that can be trapped in the grid, assuming that water can only flow horizontally and vertically. The grid is rectangular and non-empty, and the input is valid.
"""

def trapped_water_volume(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    left_max = [0] * cols
    right_max = [0] * cols
    water_volume = 0

    for i in range(rows):
        cur_left_max = 0
        cur_right_max = 0

        for j in range(cols):
            left_max[j] = max(left_max[j], cur_left_max)
            cur_left_max = max(cur_left_max, grid[i][j])

            right_max[cols - 1 - j] = max(right_max[cols - 1 - j], cur_right_max)
            cur_right_max = max(cur_right_max, grid[i][cols - 1 - j])

        for j in range(cols):
            height = min(left_max[j], right_max[j]) - grid[i][j]
            if height > 0:
                water_volume += height

    return water_volume