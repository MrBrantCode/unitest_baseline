"""
QUESTION:
Implement a function `solve_sudoku` that solves a given Sudoku puzzle of size N x N. The function should take a 2D list representing the puzzle as input and return True if a solution is found, and False otherwise. The puzzle is solved when each row, column, and subgrid contains all numbers from 1 to N without repetition. The function should handle puzzles with a size of up to 100 x 100 within a reasonable time frame. The puzzle is represented as a 2D list where 0 represents an empty cell.
"""

def solve_sudoku(puzzle):
    n = len(puzzle)
    n_sqrt = int(n ** 0.5)

    def is_valid(num, row, col):
        # Check if num is already in the row
        if num in puzzle[row]:
            return False

        # Check if num is already in the column
        if num in [puzzle[i][col] for i in range(n)]:
            return False

        # Check if num is already in the subgrid
        subgrid_row = (row // n_sqrt) * n_sqrt
        subgrid_col = (col // n_sqrt) * n_sqrt
        for i in range(subgrid_row, subgrid_row + n_sqrt):
            for j in range(subgrid_col, subgrid_col + n_sqrt):
                if puzzle[i][j] == num:
                    return False

        return True

    def find_empty_cell():
        for i in range(n):
            for j in range(n):
                if puzzle[i][j] == 0:
                    return i, j
        return -1, -1

    def solve():
        row, col = find_empty_cell()
        if row == -1 and col == -1:
            return True

        for num in range(1, n + 1):
            if is_valid(num, row, col):
                puzzle[row][col] = num

                if solve():
                    return True

                puzzle[row][col] = 0

        return False

    return solve()