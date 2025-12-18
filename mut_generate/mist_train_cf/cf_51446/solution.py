"""
QUESTION:
Write a function named `countBattleships(board)` that takes a 2D list `board` containing 'X' and '.' characters as input. The function should return the number of battleships in the board, where battleships are represented by 'X' characters, and are separated by at least one empty slot represented by '.' characters. The function should run in one-pass and use O(1) extra memory.
"""

def countBattleships(board):
    if not board:
        return 0

    count = 0
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'X':
                
                if r>0 and board[r-1][c] == 'X':   # If 'X' to the top
                    continue
                    
                if c>0 and board[r][c-1] == 'X':   # If 'X' to the left        
                    continue
                
                count += 1
                
    return count