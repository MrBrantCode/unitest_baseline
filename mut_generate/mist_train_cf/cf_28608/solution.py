"""
QUESTION:
Write a function `largest_square_root` that takes a non-negative integer `x` as input and returns the largest integer whose square is less than or equal to `x`. The function should use a binary search algorithm to find the result. The input `x` is guaranteed to be a non-negative integer.
"""

def largest_square_root(x):
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square <= x:
            left = mid + 1
        elif square > x:
            right = mid - 1
    return left - 1