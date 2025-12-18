"""
QUESTION:
Write a function `maximizePoints(grid: List[List[int]]) -> int` to calculate the maximum points that can be earned by placing 2x2 tiles on a grid where each cell contains non-negative integers representing the points earned by placing a tile on that cell. The grid has dimensions m x n where 1 <= m, n <= 100.
"""

from typing import List

def maximizePoints(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    max_points = 0
    for i in range(m - 1):
        for j in range(n - 1):
            points = grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1]
            max_points = max(max_points, points)
    return max_points