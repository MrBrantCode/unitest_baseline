"""
QUESTION:
Write a function `sqrt(x)` that calculates the square root of a given number `x` using binary search and recursion. The function should return the square root with up to 5 decimal places for real numbers and in the format `xj` for complex numbers. The input `x` can be any real number. The function should handle edge cases and have a time complexity of O(log n) and space complexity of O(log n) considering the system stack used for recursion.
"""

def sqrt(x):
    # handling edge cases
    if x == 0 or x == 1:
        return x

    # sqrt for real number
    elif x > 0:
        low, high, eps = 0, x, 0.00001
        while abs(low - high) > eps:
            mid = (low + high) / 2
            if mid * mid < x:
                low = mid
            else:
                high = mid
        return round((low + high) / 2, 5)

    # sqrt for complex number
    elif x < 0:
        x = -x
        low, high, eps = 0, x, 0.00001
        while abs(low - high) > eps:
            mid = (low + high) / 2
            if mid * mid < x:
                low = mid
            else:
                high = mid
        return str(round((low + high) / 2, 5))+"j"