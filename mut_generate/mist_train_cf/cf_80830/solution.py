"""
QUESTION:
Create a function named `is_safe_toroidal` that checks if a queen can be safely placed at a given position on a toroidal chessboard of size NxN without being threatened by any other queens. The function should take as input the current state of the board, the row and column of the position to check, and the size of the board N. The function should return True if the queen can be safely placed and False otherwise.
"""

def is_safe_toroidal(board, row, col, N):
    # Check this row on left and right side
    for i in range(N):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left and right side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i % N][j % N] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i % N][j % N] == 1:
            return False

    # Check lower diagonal on left and right side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i % N][j % N] == 1:
            return False
    for i, j in zip(range(row, N), range(col, N)):
        if board[i % N][j % N] == 1:
            return False

    return True