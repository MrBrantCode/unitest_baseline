"""
QUESTION:
Write a function `matrix_operations(matrix)` that takes a 3x3 matrix (a list of lists) as input and returns a tuple containing the sum of all even numbers in the matrix, the sum of the elements in the third column, and the largest number in the second row.
"""

def entrance(matrix):
    sum_even = sum(num for row in matrix for num in row if num % 2 == 0)
    sum_third_column = sum(row[2] for row in matrix)
    max_second_row = max(matrix[1])
    return (sum_even, sum_third_column, max_second_row)