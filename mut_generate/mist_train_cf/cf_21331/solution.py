"""
QUESTION:
Create a function named `print_spiral` that prints the elements of a given 2D matrix in a clockwise spiral order using a recursive approach. The matrix can be of any size and may contain negative numbers.
"""

def print_spiral(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    def print_spiral_recursive(start_row, end_row, start_col, end_col):
        if start_row > end_row or start_col > end_col:
            return
        
        for col in range(start_col, end_col + 1):
            print(matrix[start_row][col], end=" ")
        
        for row in range(start_row + 1, end_row + 1):
            print(matrix[row][end_col], end=" ")
        
        if start_row < end_row:
            for col in range(end_col - 1, start_col - 1, -1):
                print(matrix[end_row][col], end=" ")
        
        if start_col < end_col:
            for row in range(end_row - 1, start_row, -1):
                print(matrix[row][start_col], end=" ")
        
        print_spiral_recursive(start_row + 1, end_row - 1, start_col + 1, end_col - 1)
    
    print_spiral_recursive(0, rows - 1, 0, cols - 1)