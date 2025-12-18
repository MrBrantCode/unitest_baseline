"""
QUESTION:
Implement a function `isValidTicTacToe(board)` that takes in a 3x3 Tic-Tac-Toe board represented as an array of strings and returns `True` if the board represents a valid game of Tic-Tac-Toe, and `False` otherwise. The game is valid if it meets the following conditions: the number of "X" characters is either equal to the number of "O" characters or one more; the game has ended with a winner (three of the same character in a row, column, or diagonal) or all squares are non-empty; and no more moves can be played if the game is over.
"""

def isValidTicTacToe(board):
    def check_winner(player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    if o_count not in {x_count - 1, x_count}:
        return False 

    x_wins = check_winner('X')
    o_wins = check_winner('O')
    if x_wins and o_wins:
        return False 
    if x_wins and x_count != o_count + 1:
        return False 
    if o_wins and x_count != o_count:
        return False 

    empty_count = sum(row.count(' ') for row in board)
    if not x_wins and not o_wins and empty_count != 0:
        return True
    else:
        return empty_count == 0