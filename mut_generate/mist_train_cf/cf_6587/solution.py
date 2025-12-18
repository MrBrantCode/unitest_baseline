"""
QUESTION:
Write a backtracking algorithm to solve the N-Queens problem with a time complexity of O(N!) and a space complexity of O(N^2). The function should be named `n_queens` and it should take one argument `n`, which is the size of the chessboard. The function should return the solution with the minimum sum of the values in the cells threatened by the queens. Each queen must be placed in such a way that no two queens threaten each other and the sum of the values in the cells it threatens is minimized. The value of a cell is determined by its coordinates, where the top-left cell has coordinates (0, 0) and the bottom-right cell has coordinates (n-1, n-1).
"""

def n_queens(n):
    def is_safe(row, col, queens):
        for r, c in queens:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def sum_threatened_cells(queen, n):
        row, col = queen
        return row + col

    def backtrack(queens):
        if len(queens) == n:
            total_sum = sum(sum_threatened_cells(queen, n) for queen in queens)
            nonlocal min_sum, min_solution
            if total_sum < min_sum:
                min_sum = total_sum
                min_solution = queens[:]
            return
        row = len(queens)
        for col in range(n):
            if is_safe(row, col, queens):
                queens.append((row, col))
                backtrack(queens)
                queens.pop()

    min_sum = float('inf')
    min_solution = []
    backtrack([])
    return min_solution