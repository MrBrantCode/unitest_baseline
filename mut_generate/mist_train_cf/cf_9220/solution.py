"""
QUESTION:
Implement a function `solve_sudoku(board)` that solves a given Sudoku puzzle using a backtracking algorithm. The function should take a 9x9 Sudoku board as input, where 0 represents an empty cell, and return `True` if a solution is found and `False` otherwise. The function should modify the input board to represent the solution if one is found.
"""

def solve_sudoku(board):
    def find_empty_cell(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    def is_valid(board, row, col, num):
        if num in board[row]:
            return False
        if num in [board[i][col] for i in range(9)]:
            return False
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[subgrid_row+i][subgrid_col+j] == num:
                    return False
        return True

    if not find_empty_cell(board):
        return True

    row, col = find_empty_cell(board)
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False