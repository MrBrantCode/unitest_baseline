"""
QUESTION:
Write a function `totalNQueens` that takes an integer `n` as input, where `1 <= n <= 9`, and returns the number of unique solutions to the n-queens problem with the supplementary stipulation that no trio of queens should align in a straight line at any angle.
"""

def totalNQueens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            return 1
        else:
            count = 0
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    count += backtrack(board, row + 1)
            return count

    board = [-1] * n
    return backtrack(board, 0)