"""
QUESTION:
Implement a function `solve_sudoku` that takes a 9x9 2D list representing a partially filled Sudoku grid as input, where empty cells are denoted by 0, and returns the solved Sudoku grid as a 9x9 2D list, ensuring each row, column, and 3x3 subgrid contains all digits from 1 to 9 without repetition.
"""

from typing import List

def solve_sudoku(board: List[List[int]]) -> List[List[int]]:
    def is_valid(num: int, row: int, col: int) -> bool:
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve() -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if solve():
                                return True
                            board[row][col] = 0
                    return False
        return True

    solve()
    return board