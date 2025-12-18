"""
QUESTION:
Create a function `bitwise_add_multiply(a, b, c)` that takes three integers as input and returns the result of adding the first two integers using only bitwise operations, and then multiplying the result by the third integer also using only bitwise operations. The function should only use bitwise operators such as `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), and `>>` (right shift), and should not use arithmetic operators like `+`, `-`, `*`, `/`, etc. Assume that the input integers are non-negative.
"""

def bitwise_add_multiply(a, b, c):
    # Step 1: Add the two integers using bitwise operators
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    # Step 2: Multiply the result by the third integer using bitwise operators
    result = 0
    for _ in range(c):
        result = add(result, a)

    return result

def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x