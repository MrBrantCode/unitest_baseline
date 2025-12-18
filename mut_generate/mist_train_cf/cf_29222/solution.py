"""
QUESTION:
Write a function `validate_battleship_board` that takes a 2D grid of characters representing a Battleship game board as input, where 'O' represents an empty space and 'X' represents a part of a battleship. The function should return `True` if the battleship board is valid and `False` otherwise, following these rules: 
- Battleships can only be placed horizontally or vertically.
- Battleships cannot touch each other, even at a corner.
"""

from typing import List

def validate_battleship_board(board: List[List[str]]) -> bool:
    rows, cols = len(board), len(board[0])
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'X':
                if (i > 0 and board[i-1][j] == 'X') or (j > 0 and board[i][j-1] == 'X'):
                    return False
                k = 1
                while j + k < cols and board[i][j+k] == 'X':
                    k += 1
                if k > 1:
                    for l in range(1, k):
                        if i > 0 and board[i-1][j+l] == 'X':
                            return False
                else:
                    k = 1
                    while i + k < rows and board[i+k][j] == 'X':
                        k += 1
                    if k > 1:
                        for l in range(1, k):
                            if j > 0 and board[i+l][j-1] == 'X':
                                return False
    return True