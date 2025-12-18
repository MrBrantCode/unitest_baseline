"""
QUESTION:
Write a function `spiral_order(matrix)` to print the spiral ordering of the input matrix. The matrix dimensions can be non-square. The function should handle empty matrices and not modify the original input. Implement the function without using the `pop()` method.
"""

def entrance(matrix):
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