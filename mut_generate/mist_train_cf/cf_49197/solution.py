"""
QUESTION:
Generate a function `zigzag(m, n)` that creates an m x n two-dimensional array filled with integers from 1 to m*n in a zig-zag pattern. The zig-zag pattern is achieved by alternating the direction of filling the array for each diagonal from top-left to bottom-right. The function should return the resulting 2D array.
"""

def zigzag(m, n):
    result = [[0] * n for _ in range(m)]
    current = 1
    for i in range(m + n -1):
        low_limit = max(0, i - n + 1)
        high_limit = min(i + 1, m)
        if i % 2 == 0:
            for j in range(low_limit, high_limit):
                result[j][i - j] = current
                current += 1
        else:
            for j in range(high_limit - 1, low_limit - 1, -1):
                result[j][i - j] = current
                current += 1
    return result