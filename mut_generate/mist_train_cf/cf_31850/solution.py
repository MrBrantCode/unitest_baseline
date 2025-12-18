"""
QUESTION:
Implement a function `unique_paths_with_obstacles(obstacle_grid)` that calculates the total number of unique paths to reach the bottom-right corner of a grid from the top-left corner, where you can only move either down or to the right. The grid is represented as a 2D list of integers where 1 indicates an obstacle and 0 indicates an empty cell. The dimensions of the grid are m x n, where 1 <= m, n <= 100. If the starting cell or the destination cell is an obstacle, return 0.
"""

def unique_paths_with_obstacles(obstacle_grid):
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    
    if obstacle_grid[0][0] == 1:
        return 0
    
    obstacle_grid[0][0] = 1
    
    for i in range(1, n):
        obstacle_grid[0][i] = 0 if obstacle_grid[0][i] == 1 else obstacle_grid[0][i-1]
    
    for i in range(1, m):
        obstacle_grid[i][0] = 0 if obstacle_grid[i][0] == 1 else obstacle_grid[i-1][0]
    
    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] == 1:
                obstacle_grid[i][j] = 0
            else:
                obstacle_grid[i][j] = obstacle_grid[i-1][j] + obstacle_grid[i][j-1]
    
    return obstacle_grid[m-1][n-1]