"""
QUESTION:
Implement a function `sudoku_solver(grid)` that uses a multi-step backtracking algorithm to solve a given 9x9 Sudoku puzzle represented by a 2D list `grid`, where 0 indicates an empty cell. The function should return `True` if a solution exists, and `False` otherwise. The function should modify the input grid in-place to represent the solution.
"""

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return -1, -1


def is_safe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


def sudoku_solver(grid):
    row, col = find_empty_location(grid)

    if row == -1 and col == -1:
        return True

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if sudoku_solver(grid):
                return True

            # Undo decision and backtrack
            grid[row][col] = 0
    return False