"""
QUESTION:
Create a function named `has_won(board, player)` that checks if a player has won in a Tic Tac Toe game. The `board` is a 3x3 list of lists, and the `player` is either 'X' or 'O'. The function should return `True` if the player has won and `False` otherwise. The winning conditions include having three of the player's symbols in a row, column, or diagonal.
"""

def has_won(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False