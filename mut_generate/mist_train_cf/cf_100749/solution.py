"""
QUESTION:
Implement a function `check_constraint(cell, board)` that checks if any cells in a radius of 2 cells from the given cell have more than 3 potential mines on a 10x10 Minesweeper game board. The function should return `True` if the move is valid and `False` otherwise. The board can be represented as a 2D list, where each cell contains the number of potential mines. The cell coordinates are 0-indexed and the origin is at the top-left corner. The radius of 2 cells means the function should check all cells that are 2 cells away from the given cell in all directions (horizontally, vertically, and diagonally).
"""

def check_constraint(cell, board):
    x, y = cell
    radius = 2
    count = 0
    
    for i in range(max(0, x - radius), min(len(board), x + radius + 1)):
        for j in range(max(0, y - radius), min(len(board[0]), y + radius + 1)):
            if board[i][j] > 3:
                return False
                
    return True