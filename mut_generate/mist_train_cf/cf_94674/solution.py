"""
QUESTION:
Write a function named `spiral_order` that takes a 2D array (n x n) as input and returns a list of its elements in a spiral order, starting from the top-left corner and going clockwise. You are not allowed to use any built-in functions or libraries that solve this problem directly.
"""

def spiral_order(matrix):
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