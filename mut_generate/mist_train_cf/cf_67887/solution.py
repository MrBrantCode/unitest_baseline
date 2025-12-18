"""
QUESTION:
Write a function `solve_sudoku(board)` that solves a given Sudoku puzzle represented as a 2D array `board` and returns a boolean indicating whether a solution exists. The function should modify the input `board` to contain the solution if it exists. The `board` is a 9x9 grid, where 0 represents an empty cell and numbers 1-9 represent filled cells. The function should use a backtracking algorithm to find a valid solution.
"""

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
             
    for x in range(9):
        if board[x][col] == num:
            return False
 
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True
 
def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True