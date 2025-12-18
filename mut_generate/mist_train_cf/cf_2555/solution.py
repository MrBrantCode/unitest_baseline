"""
QUESTION:
Write a function `add_multiply(a, b, c)` that takes three integers as input, adds the first two integers using only bitwise operations, and then multiplies the result by 2 raised to the power of the third integer. The function should have a time complexity of O(log(n)) and a space complexity of O(1).
"""

def add_multiply(a, b, c):
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    return a << c