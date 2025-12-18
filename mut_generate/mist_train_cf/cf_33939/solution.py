"""
QUESTION:
Implement a function `explore` that takes a 2D grid and a starting position (row, col) as input, and returns the number of reachable empty cells from the starting position, considering movements in all four cardinal directions (up, down, left, right) but not diagonally. The grid represents a map with obstacles, where 0 denotes an empty cell and 1 denotes a blocked cell. The function should not revisit the same cell more than once.
"""

def explore(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 0:
        return 0  # Base case: out of bounds or obstacle encountered

    count = 1  # Count the current cell as reachable
    grid[row][col] = -1  # Mark the cell as visited

    # Recursively explore in all four directions
    count += explore(grid, row+1, col)  # Down
    count += explore(grid, row-1, col)  # Up
    count += explore(grid, row, col+1)  # Right
    count += explore(grid, row, col-1)  # Left

    return count