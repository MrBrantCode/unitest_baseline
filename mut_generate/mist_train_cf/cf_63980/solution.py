"""
QUESTION:
Implement a function `spiral_matrix(matrix)` that takes a 2D array as input and returns a list of elements in a spiral pattern. The input matrix is a list of lists where each inner list represents a row in the matrix. The function should return a list containing all elements of the input matrix in the order they appear in a spiral traversal of the matrix, starting from the top left corner and moving right, then down, then left, then up, and so on, until all elements have been visited.
"""

def entance(matrix):
    pattern = []
    while matrix:
        pattern += matrix.pop(0)
        if matrix and matrix[0]:
            for i in matrix:
                pattern.append(i.pop())
        if matrix:
            pattern += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for i in matrix[::-1]:
                pattern.append(i.pop(0))
    return pattern