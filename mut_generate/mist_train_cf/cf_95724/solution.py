"""
QUESTION:
Implement a function named `solve_sudoku` that takes a 9x9 partially filled Sudoku grid as input and returns a solved Sudoku grid. The input grid is guaranteed to have a valid solution. The function should be able to solve the Sudoku grid within a reasonable time limit. The grid is represented as a 2D list of integers, where 0 represents an empty cell.
"""

def solve_sudoku(grid):
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
        if num in grid[row]:
            return False
        for i in range(9):
            if grid[i][col] == num:
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False
        return True

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