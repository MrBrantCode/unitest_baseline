"""
QUESTION:
Write a function named `solve_n_queens` that takes an integer `n` as input and returns all possible configurations of an `n x n` chessboard where `n` queens can be placed such that no two queens are in the same row, column, or diagonal.
"""

def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board)
    
    result = []
    place_queens(n, 0, [-1]*n)
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]