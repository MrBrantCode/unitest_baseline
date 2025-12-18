"""
QUESTION:
Write a function named `add_without_operator(a, b)` that takes two positive integers `a` and `b` less than 100, and returns their sum without using the addition operator or any mathematical operators.
"""

def add_without_operator(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a