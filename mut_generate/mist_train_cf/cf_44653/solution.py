"""
QUESTION:
Write a function `solveSudoku(board)` that takes a 9x9 Sudoku grid as input and fills in the empty cells with the numbers 1-9 such that each row, column, and 3x3 sub-grid contains each number exactly once. The input grid is represented as a 2D list of strings, where "." represents an empty cell. The function should modify the input grid in-place to contain the solved Sudoku puzzle. The input grid is guaranteed to have a unique solution.
"""

def solveSudoku(board):
    def is_valid(board, row, col, num):
        for x in range(9):
            if board[row][x] == num:
                return False
        for x in range(9):
            if board[x][col] == num:
                return False
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in "123456789":
                        if is_valid(board, i, j, num):
                            board[i][j] = num  
                            if solve(board):  
                                return True
                            else:
                                board[i][j] = "."  
                    return False  
        return True  

    if board:
        solve(board)