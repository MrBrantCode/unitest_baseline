"""
QUESTION:
Write a function called `print_spiral_recursive` to print the elements of a given 2D matrix in a clockwise spiral order. The function should handle matrices of any size and include negative numbers. The approach should be recursive. The function should take five parameters: a 2D matrix and four integers representing the start and end row and column indices of the current sub-matrix being processed.
"""

def print_spiral_recursive(matrix, start_row, end_row, start_col, end_col):
    # Base case: If the start_row or start_col becomes greater than the end_row or end_col respectively,
    # it means we have traversed the entire matrix
    if start_row > end_row or start_col > end_col:
        return
    
    # Print the top row
    for col in range(start_col, end_col + 1):
        print(matrix[start_row][col], end=" ")
    
    # Print the right column
    for row in range(start_row + 1, end_row + 1):
        print(matrix[row][end_col], end=" ")
    
    # Print the bottom row
    if start_row < end_row:
        for col in range(end_col - 1, start_col - 1, -1):
            print(matrix[end_row][col], end=" ")
    
    # Print the left column
    if start_col < end_col:
        for row in range(end_row - 1, start_row, -1):
            print(matrix[row][start_col], end=" ")
    
    # Recursively call the function on the inner matrix
    print_spiral_recursive(matrix, start_row + 1, end_row - 1, start_col + 1, end_col - 1)