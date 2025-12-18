"""
QUESTION:
Given an integer `n`, write a function `n_queens_quadrant` that returns all possible configurations of an `n x n` chessboard such that `n` queens are placed on the board, with no two queens in the same row, column, or diagonal, and at least one queen in each quadrant. Assume `n` is an even number greater than 1.
"""

def n_queens_quadrant(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 1:
                return False
        return True

    def place_queens(board, row, cols, pos_diags, neg_diags, quadrant, res):
        if row == n:
            res.append([''.join(['Q' if c == 1 else '.' for c in r]) for r in board])
            return
        for col in range(n):
            if col in cols or row - col in pos_diags or row + col in neg_diags:
                continue
            if quadrant == 1 and (col < n // 2 or row < n // 2):
                continue
            if quadrant == 2 and (col >= n // 2 or row < n // 2):
                continue
            if quadrant == 3 and (col < n // 2 or row >= n // 2):
                continue
            if quadrant == 4 and (col >= n // 2 or row >= n // 2):
                continue
            board[row][col] = 1
            cols.add(col)
            pos_diags.add(row - col)
            neg_diags.add(row + col)
            place_queens(board, row + 1, cols, pos_diags, neg_diags, quadrant, res)
            board[row][col] = 0
            cols.remove(col)
            pos_diags.remove(row - col)
            neg_diags.remove(row + col)

    def solve_quadrant(quadrant):
        res = []
        board = [[0] * n for _ in range(n)]
        place_queens(board, 0, set(), set(), set(), quadrant, res)
        return res

    res = []
    for i in range(1, 5):
        solutions = solve_quadrant(i)
        for solution in solutions:
            res.append(solution)
    return res