"""
QUESTION:
Create a function `check_winner(board)` that takes a 3x3 list of lists representing a Tic Tac Toe game board as input. The board is populated with 'X', 'O', or ' ' (empty space). The function should return True if there is a winner (either 'X' or 'O' has three in a row, column, or diagonal) and False otherwise.
"""

def check_winner(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=' ': 
            return True
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=' ': 
            return True
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=' ': 
        return True
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=' ': 
        return True
    return False