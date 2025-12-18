"""
QUESTION:
Write a function called `spiral_order` that takes a 2D list `matrix` as input and returns a list of its elements in a spiral order, starting from the top left. The function should iterate through the matrix in a vortex-shaped pattern, moving right, down, left, and up, and append the elements to the result list in the order they are visited. The function should handle square matrices of any size.
"""

def spiral_order(matrix):
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