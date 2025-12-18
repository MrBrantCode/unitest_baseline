"""
QUESTION:
Given a 2D grid representing a game board where 1 denotes an open space and 0 denotes an obstacle, write a function `shortestPath` that takes in the grid as a list of lists and returns the length of the shortest path from the top-left corner to the bottom-right corner moving in four directions (up, down, left, right) through open spaces. If a path exists, return its length; otherwise, return -1.
"""

from typing import List
from collections import deque

def shortestPath(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    while queue:
        row, col, path_length = queue.popleft()
        if row == rows - 1 and col == cols - 1:
            return path_length
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                queue.append((new_row, new_col, path_length + 1))
                grid[new_row][new_col] = 0  # Mark as visited to avoid revisiting

    return -1