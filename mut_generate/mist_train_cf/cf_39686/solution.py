"""
QUESTION:
Implement a function `check_winner(board)` that takes a 3x3 list representing a Tic-Tac-Toe game board as input and returns a boolean value indicating whether the game is over (i.e., a player has won or the game has ended in a draw). The game board is represented by 'X' for Player 1, 'O' for Player 2, and ' ' for an empty space. The function should check for a winning condition in horizontal, vertical, or diagonal lines.
"""

def check_winner(board):
    # Check rows and columns for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    # If no winner, check for a draw
    if all([cell != ' ' for row in board for cell in row]):
        return True  # Game ends in a draw

    return False  # No winner yet