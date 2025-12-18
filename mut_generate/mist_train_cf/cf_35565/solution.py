"""
QUESTION:
Create a function `is_valid_sudoku(grid)` that validates a 9x9 Sudoku board represented as a 2D list. The function should return True if the board is valid and False if it is not. A valid Sudoku board has each row, column, and 3x3 subgrid containing the numbers 1 to 9 without repetition. The input grid may contain zeros to represent empty cells.
"""

def is_valid_sudoku(grid):
    def is_valid_row(row_num, num):
        return num not in grid[row_num]

    def is_valid_col(col_num, num):
        for row in range(9):
            if grid[row][col_num] == num:
                return False
        return True

    def is_valid_box(start_row, start_col, num):
        for row in range(3):
            for col in range(3):
                if grid[row + start_row][col + start_col] == num:
                    return False
        return True

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                num = grid[i][j]
                grid[i][j] = 0
                if not is_valid_row(i, num) or not is_valid_col(j, num) or not is_valid_box(i - i % 3, j - j % 3, num):
                    return False
                grid[i][j] = num
    return True