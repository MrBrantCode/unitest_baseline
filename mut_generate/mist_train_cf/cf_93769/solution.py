"""
QUESTION:
Implement a function named `solve_sudoku(board)` that uses a backtracking algorithm to solve a Sudoku puzzle of size N x N, where N can be any positive integer. The function should take a 2D list `board` as input, where 0 represents an empty cell. The function should return `True` if a solution exists and fill the `board` with the solution, and `False` otherwise. The solution should ensure that each row, column, and subgrid of size sqrt(N) x sqrt(N) contains all numbers from 1 to N without repetition.
"""

def is_valid(board, row, col, num):
    # Check if the same number already exists in the row
    for i in range(len(board)):
        if board[row][i] == num:
            return False

    # Check if the same number already exists in the column
    for i in range(len(board)):
        if board[i][col] == num:
            return False

    # Check if the same number already exists in the 3x3 subgrid
    subgrid_size = int(len(board) ** 0.5)
    start_row = row - (row % subgrid_size)
    start_col = col - (col % subgrid_size)
    for i in range(subgrid_size):
        for j in range(subgrid_size):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[row][col] == 0:  # Empty cell, try numbers from 1 to n
                for num in range(1, n + 1):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):  # Recursively solve the puzzle
                            return True
                        else:
                            board[row][col] = 0  # Backtrack

                return False  # No valid number found, backtrack

    return True  # All cells are filled, solution found