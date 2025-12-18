"""
QUESTION:
Write a function `solveSudoku(board)` that takes a 9x9 Sudoku board as input and returns the solved board. The input board is a 2D list of strings, where '.' represents an empty cell. The function should modify the input board in-place to contain the solution. The board is guaranteed to have a unique solution. 

The function should follow these rules:
- Each digit from '1' to '9' must appear exactly once in every row.
- Each digit from '1' to '9' must appear exactly once in every column.
- Each digit from '1' to '9' must appear exactly once in each of the 9 3x3 sub-grids of the matrix.
"""

def solveSudoku(board):
    def is_valid(board, row, col, num):
        for x in range(9):
            if board[row][x] == num:
                return False
        for x in range(9):
            if board[x][col] == num:
                return False
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + startRow][j + startCol] == num:
                    return False
        return True

    def solve(board, row, col):
        if row == 9 - 1 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if board[row][col] != '.':
            return solve(board, row, col + 1)
        for num in range(1, 10):
            if is_valid(board, row, col, str(num)):
                board[row][col] = str(num)
                if solve(board, row, col + 1):
                    return True
        board[row][col] = '.'
        return False

    if not board:
        return None
    solve(board, 0, 0)