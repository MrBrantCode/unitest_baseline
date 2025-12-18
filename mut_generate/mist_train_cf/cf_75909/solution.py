"""
QUESTION:
Implement a function `check_win(board)` that takes a 3x3 Tic Tac Toe board as input and returns `True` if there's a winner, `False` otherwise. The board is represented as a 2D list of characters where 'X' and 'O' represent the players' moves and ' ' represents an empty space.
"""

def check_win(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return True
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if len(set(check)) == 1 and check[0] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False