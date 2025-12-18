"""
QUESTION:
Design a backtracking algorithm to solve the N-queens problem, where the goal is to place N chess queens on an N x N chessboard so that no two queens threaten each other. Implement a function `n_queens(n: int)` that returns the number of possible solutions for a given N and one valid configuration for each solution found.

The function should take an integer `n` as input, representing the size of the chessboard (N x N) and the number of queens to place, where 1 ≤ n ≤ 12. The output should be a tuple containing an integer representing the number of possible solutions and a list of lists of strings, representing the valid configurations. Each configuration should be represented as a list of strings, where each string is a row of the board with a queen represented by 'Q' and empty cells represented by '.'. The implementation should avoid unnecessary branching in the solution space and be able to solve the problem for n=12 within reasonable time (less than 1 minute).
"""

def n_queens(n: int) -> (int, list):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def place_queens(board, row):
        if row == n:
            result[0] += 1
            result[1].append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                place_queens(board, row + 1)
                board[row][col] = '.'

    result = [0, []]
    board = [['.' for _ in range(n)] for _ in range(n)]
    place_queens(board, 0)
    return tuple(result)