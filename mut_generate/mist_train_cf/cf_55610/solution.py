"""
QUESTION:
Write a function `solve_n_rooks(n)` to place N rooks on an N×N chessboard so that no two rooks threaten each other, i.e., there should be no two rooks in the same row or column. The function should return the configuration of the board as a 2D array or print "Solution does not exist" if a solution does not exist.
"""

def solve_n_rooks(n):
    board = [[0]*n for _ in range(n)]

    def is_safe(row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        return True

    def solve_util(col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(i, col):
                board[i][col] = 1
                if solve_util(col + 1):
                    return True
                board[i][col] = 0
        return False

    if not solve_util(0):
        return "Solution does not exist"
    return board