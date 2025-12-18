"""
QUESTION:
Write a function `max_column_sum` that takes an array of 100 integers as input and divides it into 25 columns. Calculate the sum of each column, and return the index of the column with the highest sum. The function should assume that the array will be rearranged into a 25x4 matrix, with any remaining elements distributed as evenly as possible across the columns.
"""

def max_column_sum(numbers):
    matrix = [[0] * 4 for _ in range(25)]
    
    for i, num in enumerate(numbers):
        row = i % 25  
        col = i // 25  
        matrix[row][col] = num
        
    column_sums = [sum(column) for column in zip(*matrix)]
    return column_sums.index(max(column_sums))