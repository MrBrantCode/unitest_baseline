"""
QUESTION:
Implement a function `print_spiral(matrix)` that prints a 2D array in a spiral form. The input matrix can range from 5x5 to 10x10 and the function should not mutate the original matrix. The function should return a list of elements in spiral order.
"""

def print_spiral(matrix):
    output = []
    while matrix:
        output += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                output.append(row.pop())
        if matrix:
            output += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                output.append(row.pop(0))
    return output