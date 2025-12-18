"""
QUESTION:
Write a function named `spiralOrder` that takes a 2D array `matrix` of size MxN as input and prints its elements in a spiral order. The function should start printing from the top left, then move right, then down, then left, and finally up in a spiral manner until all elements have been printed.
"""

def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse from bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result