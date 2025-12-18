"""
QUESTION:
Implement a function `gameSimulation(grid)` that takes a 2D array `grid` as input, where each cell can contain one of the following symbols: '.' (empty space), '#' (obstacle), 'E' (exit point), or 'I' (item). The player can move in four directions: up, down, left, and right, but cannot move outside the grid or through obstacles. The function should return the maximum number of items the player can collect while reaching the exit point. If the exit point is unreachable, the function should return -1.
"""

from typing import List

def entrance(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#'

    def dfs(x, y, items_collected):
        if not is_valid_move(x, y):
            return -1
        if grid[x][y] == 'E':
            return items_collected
        if grid[x][y] == 'I':
            items_collected += 1
        max_items = -1
        original = grid[x][y]
        grid[x][y] = '#'  # Mark as visited
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            result = dfs(new_x, new_y, items_collected)
            if result != -1 and result > max_items:
                max_items = result
        grid[x][y] = original  # Backtrack
        return max_items

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                result = dfs(i, j, 0)
                if result != -1:
                    return result
    return -1