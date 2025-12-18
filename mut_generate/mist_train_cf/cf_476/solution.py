"""
QUESTION:
Write a function named `solve_sudoku` that solves a Sudoku puzzle of size N x N using the backtracking algorithm. The function should take a 2D list representing the puzzle as input, where 0 indicates an empty cell. The function should return True if the puzzle is solved successfully, and False otherwise. The function should ensure that each row, column, and subgrid contains all numbers from 1 to N without repetition.
"""

def solve_sudoku(puzzle):
    def is_valid(puzzle, row, col, num):
        # Check if num is already in the row
        if num in puzzle[row]:
            return False

        # Check if num is already in the column
        if num in [puzzle[i][col] for i in range(len(puzzle))]:
            return False

        # Check if num is already in the subgrid
        subgrid_size = int(len(puzzle) ** 0.5)
        subgrid_row = (row // subgrid_size) * subgrid_size
        subgrid_col = (col // subgrid_size) * subgrid_size
        for i in range(subgrid_row, subgrid_row + subgrid_size):
            for j in range(subgrid_col, subgrid_col + subgrid_size):
                if puzzle[i][j] == num:
                    return False

        return True

    def find_empty_cell(puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[i][j] == 0:
                    return i, j
        return -1, -1

    row, col = find_empty_cell(puzzle)
    if row == -1 and col == -1:
        return True

    for num in range(1, len(puzzle) + 1):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num

            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = 0

    return False