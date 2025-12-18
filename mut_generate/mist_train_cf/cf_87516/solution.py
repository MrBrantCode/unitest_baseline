"""
QUESTION:
Create a function called `add_multiply` that takes three integers `a`, `b`, and `c` as input, adds `a` and `b` using only bitwise operations, and then multiplies the result by 2 raised to the power of `c`. The function should have a time complexity of O(log(n)) and a space complexity of O(1).
"""

def add_multiply(a, b, c):
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    return a << c