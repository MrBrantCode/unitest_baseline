"""
QUESTION:
Write a function `count_valid_paths` that takes a 2D list of integers representing a maze, where 0 denotes an open cell and 1 denotes a blocked cell. The function should calculate the number of valid paths from the top-left corner to the bottom-right corner of the maze, where each move can only be to the right or down, and does not pass through any blocked cells. 

The function should return an integer representing the total count of valid paths found.
"""

from typing import List

def count_valid_paths(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def traverse_grid(i=0, j=0):
        if i > rows - 1 or j > cols - 1 or grid[i][j] == 1:
            return 0
        if i == rows - 1 and j == cols - 1:
            return 1
        return traverse_grid(i + 1, j) + traverse_grid(i, j + 1)

    return traverse_grid()