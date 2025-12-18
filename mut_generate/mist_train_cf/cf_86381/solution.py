"""
QUESTION:
Write a function named `spiral_order` that takes a two-dimensional array `matrix` as input and returns its elements in a clockwise spiral order. The function should handle arrays with uneven lengths and empty arrays without crashing or producing unexpected results. The array can have a maximum size of 1000 elements. The array can contain negative integers and decimal numbers.
"""

def spiralOrder(matrix):
    if not matrix or len(matrix[0]) == 0:
        return []

    rows, cols = len(matrix), len(matrix[0])
    size = rows * cols
    spiral = []

    left, right, top, bottom = 0, cols - 1, 0, rows - 1

    while len(spiral) < size:
        for col in range(left, right + 1):
            spiral.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            spiral.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                spiral.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                spiral.append(matrix[row][left])
            left += 1

    return spiral