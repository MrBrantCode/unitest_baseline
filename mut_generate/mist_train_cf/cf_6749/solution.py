"""
QUESTION:
Write a function named `print_spiral` that takes a 2D matrix as input, prints its elements in a clockwise spiral order, and returns the sum of all elements in the matrix. The function should handle matrices of any size, including those with negative numbers, and must be implemented using a recursive approach.
"""

def print_spiral(matrix):
    if not matrix:
        return 0

    row_start = 0
    row_end = len(matrix) - 1
    col_start = 0
    col_end = len(matrix[0]) - 1

    total_sum = 0

    def print_clockwise(matrix, row_start, row_end, col_start, col_end):
        nonlocal total_sum

        # Print the first row
        for i in range(col_start, col_end + 1):
            print(matrix[row_start][i], end=" ")
            total_sum += matrix[row_start][i]
        row_start += 1

        # Print the last column
        for i in range(row_start, row_end + 1):
            print(matrix[i][col_end], end=" ")
            total_sum += matrix[i][col_end]
        col_end -= 1

        # Print the last row, if it exists
        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                print(matrix[row_end][i], end=" ")
                total_sum += matrix[row_end][i]
            row_end -= 1

        # Print the first column, if it exists
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                print(matrix[i][col_start], end=" ")
                total_sum += matrix[i][col_start]
            col_start += 1

        # Recursive call for the inner sub-matrix
        if row_start <= row_end and col_start <= col_end:
            print_clockwise(matrix, row_start, row_end, col_start, col_end)

    print_clockwise(matrix, row_start, row_end, col_start, col_end)
    return total_sum