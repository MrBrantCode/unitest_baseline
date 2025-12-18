"""
QUESTION:
Write a function `cubic_root` that takes four parameters: `low`, `high`, `n`, and `difference`, and returns the cube root of `n` using recursion and binary search without using any built-in Python functions that directly calculate cube root. The function should return a real number solution of the equation x³ = n. If n is not a cubed integer, the function should return the closest cubed integer and its cube root accordingly. The precision of the difference should be adjustable.
"""

def cubic_root(low, high, n, difference):
    mid = (low + high) / 2.0
    cube = mid * mid * mid

    # If cube of mid is equals to n, return mid
    if (abs(cube - n) <= difference):
        return mid

    # If cube of mid is greater than n, reduce high to mid
    if (cube > n):
        return cubic_root(low, mid, n, difference)

    # Else increase low to mid
    else:
        return cubic_root(mid, high, n, difference)