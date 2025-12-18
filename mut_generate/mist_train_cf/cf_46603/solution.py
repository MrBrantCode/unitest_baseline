"""
QUESTION:
Write a function `solve(board)` that solves a 9x9 Sudoku puzzle represented by the input 2D list `board`, where zeros represent empty cells. The function should return the solved board if a solution exists, and an empty list otherwise. The input board may contain values from 1 to 9 and zeros. The function should modify the input board in-place if a solution is found.
"""

def solve(board):
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


    def solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if solve_sudoku(board):
                                return True
                            board[i][j] = 0
                    return False
        return True


    if solve_sudoku(board):
        return board
    return []