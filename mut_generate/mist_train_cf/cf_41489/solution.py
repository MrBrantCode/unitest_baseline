"""
QUESTION:
Implement a function `n_queens` that takes an integer `n` as input, representing the size of an n×n chessboard. Return all possible solutions to the N-Queens problem, where each solution is a list of length `n` representing the column position of the queen in each row, such that no two queens threaten each other by sharing the same row, column, or diagonal.
"""

def n_queens(n):
    def under_attack(col, queens):
        return col in queens or any(abs(col - x) == len(queens) - i for i, x in enumerate(queens))

    solutions = [[]]
    for i in range(n):
        solutions = [solution + [i] for solution in solutions if not under_attack(i, solution)]
    return solutions