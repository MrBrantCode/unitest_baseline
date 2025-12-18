"""
QUESTION:
Implement a function `spiralPathway(matrix)` that constructs a clockwise spiral pathway through a 2D matrix of integers. The function should take a 2D list of integers as input and return a 1D list of integers representing the spiral path. The input matrix can be of any size and may contain duplicate values. The output list should contain all elements from the input matrix in the order they appear in the clockwise spiral.
"""

def spiralPathway(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result