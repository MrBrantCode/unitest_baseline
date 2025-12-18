"""
QUESTION:
Write a function called `spiral_traversal` that takes an n x m matrix as input and returns its elements in a list after a spiral traversal. The function should have a time complexity of O(n*m) and space complexity of O(n*m). The input matrix is guaranteed to have 1 ≤ n, m ≤ 10^3 and the matrix elements can be integers ranging from -10^6 to 10^6.
"""

def spiral_traversal(matrix):
    if not matrix:
        return []

    n, m = len(matrix), len(matrix[0])
    result = []

    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    while len(result) < n * m:
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