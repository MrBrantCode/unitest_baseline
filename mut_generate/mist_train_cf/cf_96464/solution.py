"""
QUESTION:
Write a function named `solve_n_queens(n)` that takes an integer `n` as input, representing the size of an N×N chessboard, and returns all possible configurations of placing N queens on the chessboard such that no two queens threaten each other and each queen maximizes the sum of the values in the cells it threatens. The value of a cell is determined by its coordinates, where the top-left cell has coordinates (0, 0) and the bottom-right cell has coordinates (N-1, N-1).
"""

def solve_n_queens(n):
    solutions = []  # List to store the solutions
    
    def is_valid(board, row, col):
        # Check if the current position is valid
        for i in range(row):
            if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
                return False
        return True
    
    def backtrack(board, row, sum_values):
        # Base case: if all queens are placed, add the current board configuration to the solutions
        if row == n:
            solutions.append(board[:])
            return
        
        # Recursive case: try placing a queen in each column of the current row
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col  # Place the queen
                new_sum_values = sum_values + row + col  # Update the sum of the values in the threatened cells
                
                # Recursive call to place the next queen
                backtrack(board, row + 1, new_sum_values)
    
    # Initialize an empty board
    board = [-1] * n
    
    # Start the backtracking algorithm
    backtrack(board, 0, 0)
    
    return solutions