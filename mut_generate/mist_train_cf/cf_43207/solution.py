"""
QUESTION:
Create a function `tic_tac_toe_winner(board)` that takes a 2D list `board` as input, where each cell can contain 'X', 'O', or an empty space, and returns the winner of the tic-tac-toe game if there is one, or 'None' if there is no winner. The winner is the player who has three of their marks in a horizontal, vertical, or diagonal row.
"""

def tic_tac_toe_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None