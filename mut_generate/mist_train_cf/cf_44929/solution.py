"""
QUESTION:
Create a function `check_win(board)` that determines if there is a winner in a Tic Tac Toe game. The `board` is represented as a list of 9 elements, where 'X' and 'O' are the player symbols and ' ' represents an empty space. The function should return `True` if there is a winner, and `False` otherwise.
"""

def check_win(board):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), 
                      (0,3,6), (1,4,7), (2,5,8), 
                      (0,4,8), (2,4,6)]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False