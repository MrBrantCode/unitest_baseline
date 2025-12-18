"""
QUESTION:
Given a 6x6 grid representing a chessboard, write a function named `knight_moves` that takes two parameters, `row` and `col`, representing the row and column indices of a cell, both ranging from 0 to 5. The function should return the number of possible moves a knight can make from the given cell, considering the knight's L-shape movement (two squares in one direction and one square in a perpendicular direction).
"""

def knight_moves(row, col):
    possible_moves = 0
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 0 <= new_row < 6 and 0 <= new_col < 6:
            possible_moves += 1
    
    return possible_moves