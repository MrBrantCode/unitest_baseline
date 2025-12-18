"""
QUESTION:
Implement a function `solve_sudoku` that takes a 2D list representing an incomplete Sudoku board as input, where 0 represents empty cells. The function should return a 2D list representing a solved Sudoku board or an empty list if no solution exists. The function should use the Backtracking algorithm to find a valid solution, following standard Sudoku rules where each row, column, and 3x3 sub-grid can contain each digit (1-9) only once.
"""

def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using the Backtracking algorithm.

    Args:
    board (list): A 2D list representing an incomplete Sudoku board, where 0 represents empty cells.

    Returns:
    list: A 2D list representing a solved Sudoku board or an empty list if no solution exists.
    """

    def is_valid(board, row, col, num):
        # Check if the number already exists in the row or column
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False

        # Check if the number exists in the 3x3 sub-grid
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if solve(board):
                                return True
                            board[i][j] = 0
                    return False
        return True

    if solve(board):
        return board
    else:
        return []