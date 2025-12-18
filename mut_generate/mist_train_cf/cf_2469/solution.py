"""
QUESTION:
Write a function named `spiral_order` that takes a 2D array as input and returns all the elements in a spiral order, starting from the top-left corner and moving clockwise. The input array can have varying dimensions, but it will always be a square matrix (n x n). The function should not use any built-in functions or libraries that directly solve this problem.
"""

def spiralOrder(matrix):
    result = []
    if not matrix:
        return result
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result