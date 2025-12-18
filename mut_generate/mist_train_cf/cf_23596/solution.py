"""
QUESTION:
Implement a function `solve_n_queens(n)` that takes an integer `n` as input, representing the number of queens to be placed on an `n x n` chessboard. The function should return all possible configurations of the board where no queen attacks any other queen. The function should use a backtracking approach to find the solutions.
"""

def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    result = []
    backtrack([-1] * n, 0)
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]