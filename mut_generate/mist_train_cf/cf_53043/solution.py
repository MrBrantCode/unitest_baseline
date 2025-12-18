"""
QUESTION:
Create a function called `solve_sudoku` that solves a given Sudoku puzzle by filling in the empty cells. The Sudoku puzzle is represented as a 9x9 grid, where some numbers are already filled in and others are empty, denoted by '.'. The function should fill in the empty cells such that each row, column, and 3x3 sub-grid contains the numbers 1-9 without repetition. The function should modify the input grid in-place and return True if a solution exists, False otherwise.
"""

def solve_sudoku(board):
    """
    Solves a given Sudoku puzzle by filling in the empty cells.

    Args:
        board (list): A 9x9 grid representing the Sudoku puzzle.

    Returns:
        bool: True if a solution exists, False otherwise.
    """
    def is_valid(row, col, num):
        # Check the given number in the row
        for r in range(9):
            if board[r][col] == str(num):
                return False
        # Check the given number in the column
        for c in range(9):
            if board[row][c] == str(num):
                return False
        # Check the given number in the 3x3 box
        start_row, start_col = row - row % 3, col - col % 3
        for r in range(3):
            for c in range(3):
                if board[r + start_row][c + start_col] == str(num):
                    return False
        return True

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                for num in range(1, 10):  # Numbers from 1 to 9
                    if is_valid(r, c, num):
                        board[r][c] = str(num)
                        if solve_sudoku(board):
                            return True
                        else:
                            board[r][c] = '.'  # Reset the cell
                return False  # Trigger backtracking
    return True