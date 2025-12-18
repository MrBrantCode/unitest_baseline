"""
QUESTION:
Design a function called `navigate_maze` to find a path from the top-left cell to the bottom-right cell in a given N x N maze, where each cell can be either empty (0) or blocked (1). The function should return a list of tuples representing the path from start to end if it exists, or an empty list if no path exists. The path should include the start and end cells, only include adjacent cells that are not blocked, and not visit the same cell more than once. The maze can have up to 3 blocked cells, and the user cannot move diagonally.
"""

from typing import List, Tuple

def navigate_maze(maze: List[List[int]]) -> List[Tuple[int, int]]:
    def dfs(row: int, col: int, path: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if (row, col) == (len(maze)-1, len(maze[0])-1):  # Destination cell reached
            return path

        if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] != 0:
            return None  # Out of bounds or blocked cell

        maze[row][col] = -1  # Mark cell as visited

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Explore all four directions
            new_row, new_col = row + dx, col + dy
            new_path = dfs(new_row, new_col, path + [(new_row, new_col)])
            if new_path is not None:
                return new_path

        maze[row][col] = 0  # Reset cell value
        path.pop()  # Remove cell from path
        return None

    start_row, start_col = 0, 0
    path = [(start_row, start_col)]  # Initialize path with start cell

    return dfs(start_row, start_col, path) or []  # Return path or empty list if no path found