"""
QUESTION:
Given a 5x5 list of strings representing a board game, write a function `check_winner(board, steps)` that determines the winner of the game. The function should return "Player 1 wins in x steps" if player 1 has 5 in a row, column, diagonal, or spiral pattern, "Player 2 wins in x steps" if player 2 has 5 in a row, column, diagonal, or spiral pattern, and "Draw" if all cells are filled and no player has 5 in a row, column, diagonal, or spiral pattern. The function should take into account the rules that no two players can play on the same cell and the game starts with player 1.
"""

def check_winner(board, steps):
    # Check rows and columns
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] != '-':
            return f"Player {board[i][0]} wins in {steps} steps"
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] != '-':
            return f"Player {board[0][i]} wins in {steps} steps"

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] != '-':
        return f"Player {board[0][0]} wins in {steps} steps"
    if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] != '-':
        return f"Player {board[0][4]} wins in {steps} steps"

    # Check spiral pattern
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] != '-':
        return f"Player {board[0][0]} wins in {steps} steps"
    if board[0][2] == board[1][1] == board[2][0] == board[3][1] == board[4][2] != '-':
        return f"Player {board[0][2]} wins in {steps} steps"
    if board[0][2] == board[1][3] == board[2][4] == board[3][3] == board[4][2] != '-':
        return f"Player {board[0][2]} wins in {steps} steps"
    if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] != '-':
        return f"Player {board[0][4]} wins in {steps} steps"

    # Check if the game is a draw
    for row in board:
        for cell in row:
            if cell == '-':
                return ""
    return "Draw"