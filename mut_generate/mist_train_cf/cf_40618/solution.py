"""
QUESTION:
Implement a function `solve_n_queens(n: int)` that takes an integer `n` as input and returns a list of valid placements of `n` queens on an `n×n` chessboard, where no two queens threaten each other. Each placement is represented as a list of strings, where each string represents a row on the chessboard, 'Q' denotes the position of a queen, and '.' denotes an empty space. If no valid placement exists, return an empty list.
"""

from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < len(board) and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def backtrack(board, row, n, result):
        if row == n:
            result.append(["".join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1, n, result)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    result = []
    backtrack(board, 0, n, result)
    return result