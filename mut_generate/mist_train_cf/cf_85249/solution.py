"""
QUESTION:
Write a function `zigzagTraversal(matrix, dimensions)` to traverse an N-dimensional matrix in a zigzag pattern. The function should take two parameters: `matrix`, the N-dimensional matrix to be traversed, and `dimensions`, a list of integers representing the dimensions of the matrix. The function should return the traversed matrix. Note that every component array across every dimension must have equal length.
"""

def zigzagTraversal(matrix, dimensions):
    if len(dimensions) == 1: 
        if dimensions[0] % 2 == 0: 
            return matrix
        return matrix[::-1] 
    result = []
    for i in range(dimensions[0]):
        row = zigzagTraversal(matrix[i], dimensions[1:])
        if i % 2 == 0: 
            result.append(row)
        else: 
            result.append(row[::-1])
    return result