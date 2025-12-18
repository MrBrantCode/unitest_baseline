"""
QUESTION:
Create a function `validateBoard(board)` that takes a 2D array `board` of characters as input, where each cell contains 'X', 'O', or '.'. The function should return `true` if the board is valid and `false` otherwise. A board is valid if it meets the following conditions: 
- The board is a square (number of rows equals the number of columns).
- Each row and column contains an equal number of 'X's and 'O's.
- There are no more than two consecutive 'X's or 'O's in any row or column.
"""

def validateBoard(board):
    n = len(board)
    
    # Check if the board is a square
    if any(len(row) != n for row in board):
        return False
    
    # Check condition 1: Each row and column contains an equal number of 'X's and 'O's
    for i in range(n):
        if board[i].count('X') != board[i].count('O'):
            return False
        col = [board[j][i] for j in range(n)]
        if col.count('X') != col.count('O'):
            return False
    
    # Check condition 2: No more than two consecutive 'X's or 'O's in any row or column
    for i in range(n):
        for j in range(n-2):
            if board[i][j] == board[i][j+1] == board[i][j+2] != '.':
                return False
            if board[j][i] == board[j+1][i] == board[j+2][i] != '.':
                return False
    
    return True