"""
QUESTION:
Implement the function `max_score(board)` that takes a 2D array `board` as input and returns the maximum score that can be obtained by moving from the top-left cell to the bottom-right cell. You can only move right or down, collecting the score of each visited cell without visiting it again. The board contains non-negative integers representing the scores of each cell.
"""

import numpy as np

def max_score(board):
    rows, cols = board.shape
    dp = np.zeros((rows, cols), dtype=int)
    
    dp[0, 0] = board[0, 0]
    
    # Fill in the first row
    for col in range(1, cols):
        dp[0, col] = dp[0, col-1] + board[0, col]
    
    # Fill in the first column
    for row in range(1, rows):
        dp[row, 0] = dp[row-1, 0] + board[row, 0]
    
    # Fill in the rest of the table
    for row in range(1, rows):
        for col in range(1, cols):
            dp[row, col] = max(dp[row-1, col], dp[row, col-1]) + board[row, col]
    
    return dp[rows-1, cols-1]