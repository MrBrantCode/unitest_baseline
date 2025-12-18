"""
QUESTION:
Write a Python function named `solveSudoku(board)` that solves a Sudoku game using a backtracking algorithm. The function takes a 9x9 2D list `board` as input, where empty cells are represented by ".". The function should modify the input `board` in-place and return `True` if the Sudoku is solved, and `False` otherwise. Assume that the input `board` is a valid Sudoku board and that the function is initially called with a non-empty `board`.
"""

def solveSudoku(board):
    def is_valid(board, row, col, num):
        # check the number in the row
        for x in range(9):
            if board[row][x] == num:
                return False
        # check the number in the col
        for x in range(9):
            if board[x][col] == num:
                return False
        # check the number in the box
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in "123456789":
                        if is_valid(board, r, c, num):
                            board[r][c] = num 
                            if solve(board):  
                                return True  
                            else:
                                board[r][c] = "."
                    return False 
        return True 

    return solve(board)