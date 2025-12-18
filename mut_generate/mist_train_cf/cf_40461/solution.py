"""
QUESTION:
Implement a function `check_winner(board)` that checks if there is a winning row or column in a given 5x5 board. The board is represented as a list of 25 elements where each element can be either 0 or 1. A winning row or column is one where all the elements are the same (either all 0s or all 1s). The function should return `True` if there is a winning row or column, and `False` otherwise.
"""

def check_winner(board):
    def check_row(row):
        return all(elem == row[0] for elem in row)

    for i in range(5):
        if check_row(board[i*5:i*5+5]):
            return True
    for i in range(5):
        if check_row(board[i:i+21:5]):
            return True
    return False