"""
QUESTION:
Write a function `shortestPath` that determines the shortest path from the top-left corner to the bottom-right corner of a given 2D grid, avoiding obstacles. The grid contains 0s for empty spaces and 2s for obstacles. You can only move in four directions: up, down, left, and right. If a path does not exist, return -1. 

The function takes a 2D list of integers as input and returns an integer representing the length of the shortest path.
"""

from typing import List
from collections import deque

def shortestPath(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited = set((0, 0))

    while queue:
        row, col, dist = queue.popleft()

        if (row, col) == (rows - 1, cols - 1):
            return dist

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, dist + 1))
                visited.add((new_row, new_col))

    return -1