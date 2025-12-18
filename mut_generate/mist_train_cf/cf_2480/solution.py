"""
QUESTION:
Write a function named `add_without_operators(a, b)` that takes two integers `a` and `b` and returns their sum without using arithmetic operators, bitwise operators, or any other mathematical operations. The function should have a time complexity of O(1).
"""

def add_without_operators(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a