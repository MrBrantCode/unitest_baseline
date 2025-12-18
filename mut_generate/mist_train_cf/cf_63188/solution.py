"""
QUESTION:
Write a function `spiral(matrix)` that generates a clockwise spiral sequence from a given 2D matrix of integers. The function should take a 2D list of integers as input and return a 1D list of integers representing the spiral sequence. The input matrix can be of any size, but it will always be rectangular (i.e., all rows will have the same number of elements).
"""

def spiral(matrix):
    result = []
    while matrix:
        # Right
        result += matrix.pop(0)
        # Down
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        # Left
        if matrix:
            result += matrix.pop()[::-1]
        # Up
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result