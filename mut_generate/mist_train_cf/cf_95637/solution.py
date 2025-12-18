"""
QUESTION:
Write a function `sqrt(number)` that calculates the square root of a given non-negative number without using any math library functions such as `pow` or `log`. The function should have a time complexity of O(log n) and be accurate up to 8 decimal places. The input number can be a positive integer or a decimal number with up to 6 decimal places.
"""

def sqrt(number):
    low = 0
    high = number
    precision = 1e-8
    mid = 0

    while abs(mid * mid - number) > precision:
        mid = (low + high) / 2
        if mid * mid > number:
            high = mid
        else:
            low = mid

    return round(mid, 8)