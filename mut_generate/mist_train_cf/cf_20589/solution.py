"""
QUESTION:
Implement a function named `multiply` that takes two integers `a` and `b` as input and returns their product without using the '*' operator. The function should utilize bit manipulation to achieve this. The integers can be positive, negative, or zero. The function should handle these cases correctly and return the correct product.
"""

def multiply(a: int, b: int) -> int:
    result = 0

    # handle negative numbers
    negative_result = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)

    while b != 0:
        if b & 1:
            result += a

        a <<= 1
        b >>= 1

    return -result if negative_result else result