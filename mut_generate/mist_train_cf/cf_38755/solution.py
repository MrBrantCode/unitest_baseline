"""
QUESTION:
Write a function `checkWin(board, row, col, chance)` that takes in a 2D game board, the last move's row and column indices, and the player's chance (either 'X' or 'O'). The function should return `True` if the player with the given chance has won the game based on the last move, and `False` otherwise. The function should check for a winning sequence in the rows, columns, and diagonals around the last move's position, where a winning sequence is defined as a horizontal, vertical, or diagonal line of four consecutive pieces belonging to the same player.
"""

def checkWin(board, row, col, chance):
    # Check for horizontal win
    if col >= 3 and all(board[row][col-i] == chance for i in range(4)):
        return True

    # Check for vertical win
    if row >= 3 and all(board[row-i][col] == chance for i in range(4)):
        return True

    # Check for diagonal win (top-left to bottom-right)
    if row >= 3 and col >= 3 and all(board[row-i][col-i] == chance for i in range(4)):
        return True

    # Check for diagonal win (bottom-left to top-right)
    if row <= 2 and col >= 3 and all(board[row+i][col-i] == chance for i in range(4)):
        return True

    return False