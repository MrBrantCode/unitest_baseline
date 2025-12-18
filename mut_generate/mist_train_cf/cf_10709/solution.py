"""
QUESTION:
Design a function `square_root(x)` that calculates the integer square root of a given number `x` with a time complexity of O(log n). The function should return the largest integer whose square is less than or equal to `x`. Assume `x` is a non-negative integer.
"""

def entrance(x):
    # Base case
    if x == 0 or x == 1:
        return x

    # Binary search
    start = 1
    end = x
    while start <= end:
        mid = (start + end) // 2

        # If x is a perfect square
        if mid * mid == x:
            return mid

        # If mid*mid is less than x
        if mid * mid < x:
            start = mid + 1
            ans = mid

        # If mid*mid is greater than x
        else:
            end = mid - 1

    return ans