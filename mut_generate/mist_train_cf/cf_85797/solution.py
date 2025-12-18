"""
QUESTION:
Implement a function `cubic_root(num, precision)` that calculates the cube root of an arbitrarily large positive integer `num` to a specified degree of precision. The function should return the cube root rounded to the specified `precision` decimal places.
"""

def cubic_root(num: int, precision: int):
    start = 0
    end = num
    while True:
        mid = (start+end)/2
        error = abs(mid**3 - num)
        if error <= 10**-precision:
            return round(mid, precision)
        if mid**3 < num:
            start = mid
        else:
            end = mid