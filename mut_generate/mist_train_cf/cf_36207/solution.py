"""
QUESTION:
Write a function `count_walls(grid: List[str]) -> int` that takes a 2D grid represented as a list of strings as input, where '#' represents a wall and '.' represents an open space, and returns the total number of walls present in the grid.
"""

from typing import List

def count_walls(grid: List[str]) -> int:
    wall_count = 0
    for row in grid:
        wall_count += row.count('#')
    return wall_count