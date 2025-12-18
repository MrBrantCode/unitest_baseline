"""
QUESTION:
Write a function `spiral_traverse(matrix)` that takes an n x m matrix as input and returns a list of its elements in spiral order. The matrix contains integers ranging from -10^3 to 10^3, and 1 ≤ n, m ≤ 10^3.
"""

def spiral_traverse(matrix):
    if not matrix:
        return []

    n = len(matrix)
    m = len(matrix[0])
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    direction = 0  # 0: left to right, 1: top to bottom, 2: right to left, 3: bottom to top

    result = []

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4

    return result