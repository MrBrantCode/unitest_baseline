"""
QUESTION:
Write a function `count_distinct_objects(photo)` that takes a 2D grid of pixels as input where each pixel is a tuple of three integers (r, g, b) representing the red, green, and blue color values. Two pixels are considered part of the same object if they share the same color or if their colors are similar enough, with two colors considered similar if the absolute difference between their corresponding color values is less than or equal to 20. The function should return the number of distinct objects visible in the photo. The input grid has a maximum dimension of 1000x1000.
"""

from typing import List, Tuple

def count_distinct_objects(photo: List[List[Tuple[int, int, int]]]) -> int:
    def dfs(grid, i, j, color, visited):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or 
            visited[i][j] or 
            abs(grid[i][j][0] - color[0]) > 20 or 
            abs(grid[i][j][1] - color[1]) > 20 or 
            abs(grid[i][j][2] - color[2]) > 20):
            return
        visited[i][j] = True
        dfs(grid, i+1, j, color, visited)
        dfs(grid, i-1, j, color, visited)
        dfs(grid, i, j+1, color, visited)
        dfs(grid, i, j-1, color, visited)

    distinct_objects = 0
    visited = [[False for _ in range(len(photo[0]))] for _ in range(len(photo))]
    for i in range(len(photo)):
        for j in range(len(photo[0])):
            if not visited[i][j]:
                dfs(photo, i, j, photo[i][j], visited)
                distinct_objects += 1
    return distinct_objects