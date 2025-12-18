"""
QUESTION:
Write a function `add_without_sign(a, b)` that takes two integers `a` and `b` as input and returns their sum without using the + or - operators. The function should not use any mathematical operations such as multiplication, division, or exponentiation. The time complexity of the solution should be O(log n), where n is the larger of the two integers.
"""

def add_without_sign(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a