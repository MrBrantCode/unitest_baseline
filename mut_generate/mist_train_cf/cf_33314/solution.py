"""
QUESTION:
Implement the function `navigate_grid(grid, start, target)` that takes a 2D list of characters `grid`, a tuple `(row, column)` `start` representing the starting position, and a character `target` representing the target location. The function should return a boolean value indicating whether the player can reach the target from the starting position by moving through the grid to adjacent cells (up, down, left, or right) that are not blocked (represented by 'X').
"""

def navigate_grid(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 'X'

    visited = set()
    queue = [start]

    while queue:
        current = queue.pop(0)
        if grid[current[0]][current[1]] == target:
            return True
        visited.add(current)

        for dr, dc in directions:
            new_row, new_col = current[0] + dr, current[1] + dc
            if (new_row, new_col) not in visited and is_valid_move(new_row, new_col):
                queue.append((new_row, new_col))

    return False