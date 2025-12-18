"""
QUESTION:
Write a function called `count_odd_even(matrix)` that takes a 2-dimensional matrix of integers as input and returns the count of all odd and even numbers in the matrix. Additionally, write a function called `is_odd_or_even(matrix, row, col)` that determines whether a given integer at the specified location (row and col) in the matrix is odd or even and returns 'Odd' or 'Even' accordingly. The solution should have a time complexity of O(n*m) where n is the number of rows and m is the number of columns in the matrix.
"""

def count_odd_even(matrix):
    odd_count = 0
    even_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return odd_count, even_count

def is_odd_or_even(matrix, row, col):
    if matrix[row][col] % 2 == 0:
        return 'Even'
    else:
        return 'Odd'