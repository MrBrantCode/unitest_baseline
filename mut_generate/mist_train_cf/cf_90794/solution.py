"""
QUESTION:
Write a function called `solve_sudoku(board)` that takes a 2D list `board` representing a Sudoku puzzle and returns `True` if the puzzle is solvable and `False` otherwise. The function should use a backtracking algorithm to fill in the empty cells of the puzzle, considering the constraints that each row, column, and 3x3 subgrid must contain all numbers from 1 to 9 without repetition. The function should modify the input `board` to contain the solution if it exists.

The input `board` is a 9x9 2D list where 0 represents an empty cell. The function should not return anything other than a boolean value, but it may modify the input `board` to contain the solution if it exists.
"""

def solve_sudoku(board):
    def find_empty_cell(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    def is_valid(board, row, col, num):
        # Check if the number already exists in the same row
        if num in board[row]:
            return False
        
        # Check if the number already exists in the same column
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # Check if the number already exists in the same 3x3 subgrid
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[subgrid_row+i][subgrid_col+j] == num:
                    return False
        
        return True

    if not find_empty_cell(board):
        return True
    
    row, col = find_empty_cell(board)
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False