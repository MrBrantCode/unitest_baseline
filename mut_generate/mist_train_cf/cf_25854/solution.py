"""
QUESTION:
Create a function `spiral_traversal` that takes a 2D array as input and returns a one-dimensional array representing the spiral traversal of the input array. The function should traverse the array from left to right, then top to bottom, right to left, and finally bottom to top, moving in a clockwise spiral pattern.
"""

def spiral_traversal(matrix):
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