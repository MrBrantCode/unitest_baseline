"""
QUESTION:
Write a Python function `sum_matrix` that takes a 5x4 matrix of random floating-point numbers between -5 and 15 (rounded to the nearest hundredth decimal place) as input and returns the sum of all numbers in the matrix. The function should not generate the matrix itself but should work with any 5x4 matrix of numbers that meet the specified criteria. The function must handle the input matrix as a list of lists in Python.
"""

def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for num in row:
            total += num
    return total