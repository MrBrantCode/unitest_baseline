"""
QUESTION:
Write a function `solve_sudoku(board)` that takes a 9x9 2D list `board` representing the initial state of a Sudoku puzzle, where the `board` is filled with digits from 1-9 and empty cells are represented by 0. Modify the `board` in place to solve the Sudoku puzzle, ensuring that each row, column, and 3x3 subgrid contains all digits from 1 to 9.
"""

def solve_sudoku(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True