"""
QUESTION:
Write a function called `bitwise_addition` that takes two integers `a` and `b` as input and returns their sum using only bitwise operations. The function should not use any arithmetic operators (+, -, *, /) or the `+` operator, and it should have a time complexity of O(log N), where N is the maximum number of bits in the given input integers.
"""

def bitwise_addition(a, b):
    while b:
        result = a ^ b
        carry = (a & b) << 1
        a = result
        b = carry
    return a