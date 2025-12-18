"""
QUESTION:
Implement a function named `solve_sudoku` that takes a 9x9 Sudoku grid as input, where empty cells are represented by 0, and returns a solved Sudoku grid if a valid solution exists. The function should be able to handle any partially filled 9x9 Sudoku grid that has a valid solution.
"""

def is_valid(board, row, col, num):
    # Check if the number already exists in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number already exists in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number already exists in the 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            # Find an empty cell
            if board[row][col] == 0:
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        # If the number is valid, place it on the board
                        board[row][col] = num

                        # Recursively solve the rest of the grid
                        if solve_sudoku(board):
                            return True

                        # If the rest of the grid cannot be solved, backtrack
                        board[row][col] = 0

                # If no valid number can be placed, the board is unsolvable
                return False

    # If all cells are filled, the board is solved
    return True