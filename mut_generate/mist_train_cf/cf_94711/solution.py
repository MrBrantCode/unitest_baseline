"""
QUESTION:
Create a function `bitwise_add_multiply` that takes three integers `a`, `b`, and `c` as input. Using only bitwise operations, the function should add `a` and `b`, then multiply the result by `c`. Note that this function should only work with non-negative integers.
"""

def bitwise_add_multiply(a, b, c):
    # Step 1: Add the two integers using bitwise operators
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    # Step 2: Multiply the result by the third integer using bitwise operators
    result = 0
    temp_a = a
    while c > 0:
        if c & 1:
            result += temp_a
        temp_a <<= 1
        c >>= 1

    return result