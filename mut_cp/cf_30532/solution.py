"""
ORIGINAL QUESTION:
Implement the function `navigate_grid(grid, start, destination)` where:
- `grid` is a rectangular 2D list of 0s and 1s representing a grid-based world, where 0 denotes an empty cell and 1 denotes a blocked cell.
- `start` is a tuple representing the starting coordinate of the character in the grid.
- `destination` is a tuple representing the destination coordinate that the character needs to reach.

The function should return `True` if the character can reach the destination from the starting point by moving only through empty cells, and `False` otherwise.
"""

def navigate_grid(grid, start, destination):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0

    def dfs(row, col):
        if (row, col) == destination:
            return True
        if grid[row][col] == 1:
            return False
        grid[row][col] = 1  # Mark current cell as visited
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col) and dfs(new_row, new_col):
                return True
        return False

    return dfs(start[0], start[1])