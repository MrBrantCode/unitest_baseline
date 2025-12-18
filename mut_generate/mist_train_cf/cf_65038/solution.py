"""
QUESTION:
Implement a function `spiral(matrix)` that takes a 2D list of integers as input and returns a 1D list representing the elements in a clockwise spiral order. The function should process the input matrix in-place, by sequentially extracting rows and columns until all elements are visited.
"""

def spiral(matrix):
    spiral_sequence = []
    while matrix:
        spiral_sequence += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                spiral_sequence.append(row.pop())
        if matrix:
            spiral_sequence += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                spiral_sequence.append(row.pop(0))
    return spiral_sequence