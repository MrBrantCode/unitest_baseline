"""
QUESTION:
Implement a function `has_valid_path` that takes a 2D grid representing a maze as input and returns a boolean value indicating whether a valid path exists from the start cell 'S' to the end cell 'E' using depth-first search, avoiding blocked cells '#' and dead ends. The maze grid contains cells that are either empty '.' or blocked '#'. The function should navigate through the maze, avoiding blocked cells and dead ends, and return True if a valid path exists, False otherwise.
"""

from typing import List

def has_valid_path(maze: List[List[str]]) -> bool:
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] != '#'

    def dfs(x, y):
        if maze[x][y] == 'E':
            return True
        maze[x][y] = '#'  # Mark the cell as visited
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and dfs(new_x, new_y):
                return True
        return False

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                return dfs(i, j)

    return False