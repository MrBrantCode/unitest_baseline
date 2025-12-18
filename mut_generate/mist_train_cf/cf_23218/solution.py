"""
QUESTION:
Design a function `solve_sudoku(board)` to solve a 9x9 Sudoku puzzle using recursive backtracking algorithm and without using any additional data structures. The function should modify the input board in-place and return a boolean indicating whether a solution was found.

The input board is a 9x9 2D list of integers where 0 represents an empty cell and numbers 1-9 represent filled cells. The function should use a helper function `is_valid(board, num, pos)` to check if a number can be placed at a given position on the board, and another helper function `find_empty(board)` to find an empty cell on the board.

The function should try numbers 1-9 for each empty cell, and use backtracking to find a valid solution. If a solution is found, the function should return `True`; otherwise, it should return `False`.
"""

def solve_sudoku(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None