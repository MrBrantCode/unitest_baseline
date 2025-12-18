"""
QUESTION:
Write a function `numRookCaptures` that takes an 8x8 2D list `board` as input, where each element is one of the characters 'R', '.', 'B', 'p', or 'r'. The function should return the number of available captures for the white rook 'R'. The function should assume that the input board meets the constraints: the length of the board and its sublists is 8, and there is exactly one 'R' on the board.
"""

def numRookCaptures(board):
    # Find R's row
    for i in range(8):
        if 'R' in board[i]:
            row = i
            break
    # Find R's column
    col = board[row].index('R')
    
    res = 0
    # Count pawns in 4 directions
    for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
        x, y = row + i, col + j
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] == 'p':
                res += 1
                break
            if board[x][y] != '.':
                break
            x, y = x + i, y + j
    return res