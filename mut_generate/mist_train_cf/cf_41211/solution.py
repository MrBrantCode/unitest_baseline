"""
QUESTION:
Write a function `reverse` that takes an integer `x` as input and returns its reverse. If `x` is negative, return the reverse of its absolute value with a negative sign. The function must handle integers within the 32-bit signed integer range (-2^31 to 2^31 - 1) and return 0 if the reversed integer exceeds this range.
"""

def reverse(x: int) -> int:
    if x < 0:
        return -reverse(-x)
    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10
    return result if result >= -2**31 and result <= 2**31 - 1 else 0