"""
QUESTION:
Implement the `canReachEnd(maze: List[List[int]]) -> bool` function, which determines whether the player can reach the bottom-right corner from the top-left corner in a given grid-based maze. The maze is represented as a 2D grid where each cell can be either empty (0) or blocked (1). The function should return `True` if the player can reach the end and `False` otherwise. Assume the maze grid is non-empty and its dimensions are at most 100x100.
"""

from typing import List

def canReachEnd(maze: List[List[int]]) -> bool:
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or maze[row][col] == 1:
            return False
        if row == rows - 1 and col == cols - 1:
            return True
        maze[row][col] = 1  # Mark the cell as visited
        for dr, dc in directions:
            if dfs(row + dr, col + dc):
                return True
        return False

    return dfs(0, 0)