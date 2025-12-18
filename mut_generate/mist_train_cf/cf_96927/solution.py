"""
QUESTION:
Write a function `sum_rows_cols(matrix)` that takes a 2D list of integers as input and returns the sum, maximum, minimum, and average of each row and column. The function should have a time complexity of O(n * m) and a space complexity of O(n + m), where n is the number of rows and m is the number of columns in the matrix. The average values should be rounded to two decimal places. The input matrix can have variable dimensions and can contain both positive and negative numbers. It is guaranteed that the matrix will have at least one row and one column.
"""

def sum_rows_cols(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    row_sums = []
    col_sums = []
    row_max = []
    col_max = []
    row_min = []
    col_min = []
    row_avg = []
    col_avg = []
    
    for i in range(num_rows):
        row_sum = 0
        row_max_val = float('-inf')
        row_min_val = float('inf')
        for j in range(num_cols):
            row_sum += matrix[i][j]
            row_max_val = max(row_max_val, matrix[i][j])
            row_min_val = min(row_min_val, matrix[i][j])
        row_sums.append(row_sum)
        row_max.append(row_max_val)
        row_min.append(row_min_val)
        row_avg.append(round(row_sum / num_cols, 2))
    
    for j in range(num_cols):
        col_sum = 0
        col_max_val = float('-inf')
        col_min_val = float('inf')
        for i in range(num_rows):
            col_sum += matrix[i][j]
            col_max_val = max(col_max_val, matrix[i][j])
            col_min_val = min(col_min_val, matrix[i][j])
        col_sums.append(col_sum)
        col_max.append(col_max_val)
        col_min.append(col_min_val)
        col_avg.append(round(col_sum / num_rows, 2))
    
    return row_sums, col_sums, row_max, col_max, row_min, col_min, row_avg, col_avg