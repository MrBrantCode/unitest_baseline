"""
QUESTION:
Create a function `print_pattern(n)` that prints a clockwise spiral pattern of positive integers from 1 to n * n (inclusive) for a given positive integer n between 1 and 10 (inclusive), and returns the sum of all elements in the pattern.
"""

def entrance(n):
    if n < 1 or n > 10:
        return "Error: n should be between 1 and 10 (inclusive)."
    
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top_row, bottom_row = 0, n - 1
    left_column, right_column = 0, n - 1
    
    while num <= n * n:
        for i in range(left_column, right_column + 1):
            matrix[top_row][i] = num
            num += 1
        top_row += 1
        
        for i in range(top_row, bottom_row + 1):
            matrix[i][right_column] = num
            num += 1
        right_column -= 1
        
        for i in range(right_column, left_column - 1, -1):
            matrix[bottom_row][i] = num
            num += 1
        bottom_row -= 1
        
        for i in range(bottom_row, top_row - 1, -1):
            matrix[i][left_column] = num
            num += 1
        left_column += 1
    
    for row in matrix:
        for num in row:
            print(num, end='\t')
        print()
    
    total_sum = sum(sum(row) for row in matrix)
    print("Sum of all elements:", total_sum)