"""
QUESTION:
Write a function `solve_n_queens(n)` to solve the N-Queens problem, where `n` is the size of the chessboard. The function should return all possible solutions, where each solution maximizes the sum of the values in the cells threatened by the queens. No two queens should share the same row, column, or diagonal. The value of a cell is determined by its coordinates, where the top-left cell has coordinates (0, 0) and the bottom-right cell has coordinates (n-1, n-1). Each solution should be represented as a list of integers, where the index of each element represents the row and the value represents the column where the queen is placed.
"""

def solve_n_queens(n):
    solutions = []  # List to store the solutions
    
    def is_valid(board, row, col, n):
        # Check if the current position is valid
        for i in range(row):
            if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
                return False
        return True

    def backtrack(board, row, n, sum_values):
        # Base case: if all queens are placed, add the current board configuration to the solutions
        if row == n:
            solutions.append(board[:])
            return
        
        # Recursive case: try placing a queen in each column of the current row
        for col in range(n):
            if is_valid(board, row, col, n):
                board[row] = col  # Place the queen
                new_sum_values = sum_values + row + col  # Update the sum of the values in the threatened cells
                
                # Recursive call to place the next queen
                backtrack(board, row + 1, n, new_sum_values)

    # Initialize an empty board
    board = [-1] * n
    
    # Start the backtracking algorithm
    backtrack(board, 0, n, 0)
    
    return solutions