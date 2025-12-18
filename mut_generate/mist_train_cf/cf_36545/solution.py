"""
QUESTION:
Implement the function `optimize_path(grid)` that calculates the minimum total cost of moving a robot from the top-left to the bottom-right corner in a grid. The grid is a 2D array where each integer represents the cost of moving through that cell. The robot can move in four directions: up, down, left, and right.
"""

def optimize_path(grid):
    rows, cols = len(grid), len(grid[0])
    min_cost = [[float('inf')] * cols for _ in range(rows)]
    min_cost[0][0] = grid[0][0]

    for i in range(rows):
        for j in range(cols):
            if i > 0:
                min_cost[i][j] = min(min_cost[i][j], min_cost[i-1][j] + grid[i][j])
            if j > 0:
                min_cost[i][j] = min(min_cost[i][j], min_cost[i][j-1] + grid[i][j])

    return min_cost[rows-1][cols-1]