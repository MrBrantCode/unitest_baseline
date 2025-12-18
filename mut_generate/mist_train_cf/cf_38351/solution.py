"""
QUESTION:
Implement a function named `reverse` that takes a 32-bit signed integer `x` as input, reverses its digits, and returns the reversed integer as a 32-bit signed integer. If the reversed integer overflows, the function should return 0. The input integer `x` is within the range [-2^31, 2^31 - 1].
"""

def reverse(x: int) -> int:
    result = 0
    negative = x < 0
    x = abs(x)
    
    while x != 0:
        digit = x % 10
        x = x // 10
        result = result * 10 + digit
    
    if negative:
        result = -result
    
    if result < -2**31 or result > 2**31 - 1:
        return 0
    else:
        return result