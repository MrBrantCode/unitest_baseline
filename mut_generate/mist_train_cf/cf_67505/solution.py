"""
QUESTION:
Implement the is_perfect_square(x) function to determine if a given integer x is a perfect square. The function should return True if x is a perfect square and False otherwise. The input x can be any integer, and the function should handle negative numbers, zero, and positive numbers. The function should be optimized for performance.
"""

def is_perfect_square(x):
    if x < 0:
        return False
    if x == 0 or x == 1:
        return True
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        if mid_squared == x:
            return True
        elif mid_squared < x:
            low = mid + 1
        else:
            high = mid - 1
    return False