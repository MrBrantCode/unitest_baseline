"""
QUESTION:
Write a function `calculate_sum(matrix)` that takes a 2D list of integers as input and returns the sum of each row and each column separately. The matrix can have variable dimensions and can contain both positive and negative numbers. The time complexity of the solution should be O(n * m), where n is the number of rows and m is the number of columns in the matrix. The space complexity should be O(n + m), where n is the number of rows and m is the number of columns in the matrix.
"""

def calculate_sum(matrix):
    """
    This function takes a 2D list of integers as input and returns the sum of each row and each column separately.
    
    Parameters:
    matrix (list): A 2D list of integers.
    
    Returns:
    tuple: A tuple containing two lists. The first list contains the sum of each row, and the second list contains the sum of each column.
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    row_sums = [0] * num_rows
    col_sums = [0] * num_cols

    for i in range(num_rows):
        for j in range(num_cols):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]

    return row_sums, col_sums