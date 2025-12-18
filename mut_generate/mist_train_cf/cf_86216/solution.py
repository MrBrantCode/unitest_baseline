"""
QUESTION:
Write a function `reverse_matrix(matrix)` that takes a matrix of numbers as input and returns a new matrix where the order of rows and columns are reversed. The input matrix will have at least 2 rows and 2 columns, but may not be square (i.e., the number of rows and columns can be different).
"""

def entrance(matrix):
    return [row[::-1] for row in matrix[::-1]]