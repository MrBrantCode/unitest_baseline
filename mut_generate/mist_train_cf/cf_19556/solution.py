"""
QUESTION:
Write a function `solve_sudoku(grid)` that takes a 9x9 partially filled Sudoku grid as input and returns a solved Sudoku grid. The input grid will always have a valid solution. The function should be able to solve Sudoku grids within a reasonable time limit.
"""

def solve_sudoku(grid):
    if is_complete(grid):
        return grid

    row, col = find_empty_cell(grid)
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return grid
            grid[row][col] = 0

    return None

def is_complete(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return False
    return True

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_valid(grid, row, col, num):
    # Check if the number is already present in the row
    if num in grid[row]:
        return False

    # Check if the number is already present in the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number is already present in the 3x3 sub-grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True