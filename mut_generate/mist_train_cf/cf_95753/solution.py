"""
QUESTION:
Design a function navigate_maze that takes a 2D grid maze of size N x N as input, where each cell is either 0 (empty) or 1 (blocked), and returns a list of tuples representing a path from the top-left cell (0, 0) to the bottom-right cell (N-1, N-1) if such a path exists. The user can only move in four directions: up, down, left, and right, and cannot pass through blocked cells or visit the same cell more than once. If there is no path, return an empty list. The maze can have up to 3 blocked cells.
"""

from typing import List, Tuple

def navigate_maze(maze: List[List[int]]) -> List[Tuple[int, int]]:
    def dfs(row: int, col: int, path: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if (row, col) == (len(maze)-1, len(maze[0])-1):  
            return path

        if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] != 0:
            return None  

        maze[row][col] = -1  

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  
            new_row, new_col = row + dx, col + dy
            new_path = dfs(new_row, new_col, path + [(new_row, new_col)])
            if new_path is not None:
                return new_path

        maze[row][col] = 0  
        return None

    if maze[0][0] != 0:
        return []

    return dfs(0, 0, [(0, 0)]) or [] 