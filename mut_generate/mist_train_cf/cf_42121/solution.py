"""
QUESTION:
Implement the function `evolve_board(board)` that takes a 4x4 numpy array `board` representing the current state of the game board and returns a new 4x4 numpy array representing the evolved board after one move according to the 2048 game rules.
"""

import numpy as np

def evolve_board(board):
    # Helper function to perform merging and sliding in a single row or column
    def merge_and_slide(row):
        # Remove zeros from the row
        row = row[row != 0]
        # Merge adjacent cells with the same value
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
        # Slide the cells to the left
        row = row[row != 0]
        return np.concatenate((row, np.zeros(4 - len(row))), axis=0)

    # Apply merge_and_slide to each row and column
    next_board = np.array([merge_and_slide(board[i, :]) for i in range(4)])
    next_board = np.array([merge_and_slide(next_board[:, i]) for i in range(4)]).T
    return next_board