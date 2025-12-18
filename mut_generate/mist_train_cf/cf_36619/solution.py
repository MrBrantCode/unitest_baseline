"""
QUESTION:
Given a 2D grid representing land (1) and water (0), where the grid is surrounded by water on all sides, write a function `calculate_perimeter(grid)` that takes in the 2D grid as input and returns the perimeter of the land in the grid. The perimeter of the land is the length of the boundary between the land and water. The function should iterate through each cell in the grid, checking adjacent cells to determine the perimeter.
"""

from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    nx, ny = r + dx, c + dy
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                        perimeter += 0 if grid[nx][ny] else 1
                    else:
                        perimeter += 1
    return perimeter