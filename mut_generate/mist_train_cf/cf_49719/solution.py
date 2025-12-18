"""
QUESTION:
Create a function to determine if a player has won in a game of Tic-tac-toe. The function should take a 3x3 board as input, where 'X' and 'O' represent the players' moves and ' ' represents an empty space. The function should return True if a player has won and False otherwise. The win conditions are: three in a row horizontally, vertically, or diagonally.
"""

def entance(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False