"""
QUESTION:
Implement a function `solve_n_queens(n)` that takes an integer `n` as input, representing the size of a chessboard, and returns all possible distributions of `n` queens on the chessboard such that no two queens share the same row, column, or diagonal.
"""

def solve_n_queens(n):
    def is_safe(board, row, col, n):
        for i in range(row):
            if board[i][col] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False
        return True

    def solve_n_queens_util(board, row, n, solutions):
        if row == n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append((i, j))
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_n_queens_util(board, row + 1, n, solutions)
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions