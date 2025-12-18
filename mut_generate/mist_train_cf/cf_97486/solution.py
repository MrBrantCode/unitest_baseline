"""
QUESTION:
Write a function named `solve_sudoku` that solves a 9x9 Sudoku puzzle using recursive backtracking algorithm without using any additional data structures. The function should take a 2D list representing the Sudoku board as input, where 0 represents an empty cell, and return a boolean indicating whether the puzzle has been solved. The function should also modify the input board to contain the solution if the puzzle is solvable.
"""

def solve_sudoku(board):
    def is_valid(num, pos):
        row, col = pos
        # Check row
        for i in range(len(board[0])):
            if board[row][i] == num and col != i:
                return False

        # Check column
        for i in range(len(board)):
            if board[i][col] == num and row != i:
                return False

        # Check 3x3 box
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty():
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)
        return None

    empty = find_empty()

    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False