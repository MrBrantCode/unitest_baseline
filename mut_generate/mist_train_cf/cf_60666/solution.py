"""
QUESTION:
Design a function `solve_sudoku(board)` that solves a standard Sudoku puzzle of size `n x n` where `n` is a perfect square, represented as a 2D array `board` where empty slots are denoted by zeros. The function should fill the `board` with numbers from 1 to `n` such that each row, column, and `sqrt(n) x sqrt(n)` sub-grid contains each number exactly once.
"""

def solve_sudoku(board):
    n = len(board)
    def is_safe(row, col, num):
        for x in range(n):
            if board[row][x] == num or board[x][col] == num:
                return False

        subgrid_size = int(n**0.5)
        start_row, start_col = row - row%subgrid_size, col - col%subgrid_size
        for i in range(subgrid_size):
            for j in range(subgrid_size):
                if board[i+start_row][j+start_col] == num:
                    return False

        return True

    def solve():
        empty = True
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    row = i
                    col = j
                    empty = False
                    break
            if not empty:
                break

        if empty:
            return True

        for num in range(1, n+1):
            if is_safe(row, col, num):
                board[row][col] = num  
                if solve():
                    return True
                board[row][col] = 0
        return False

    return solve()