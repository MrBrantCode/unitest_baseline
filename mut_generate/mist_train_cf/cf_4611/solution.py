"""
QUESTION:
Write a function `square_root(n)` that computes the square root of a positive integer `n` without using the square root function or any math library functions. The solution should have a time complexity of O(log n) and be accurate up to 10 decimal places.
"""

def square_root(n):
    # Base cases for 0 and 1
    if n == 0 or n == 1:
        return n

    # Binary search algorithm
    low = 0
    high = n

    while high - low > 1e-11:  # Accuracy up to 10 decimal places
        mid = (low + high) / 2
        square = mid * mid

        if square == n:
            return round(mid, 10)
        elif square < n:
            low = mid
        else:
            high = mid

    return round(low, 10)