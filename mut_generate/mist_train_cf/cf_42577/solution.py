"""
QUESTION:
Implement a function `add_without_plus(num1, num2)` that takes two positive integers `num1` and `num2` as input and returns their sum using only bitwise operations, without utilizing the '+' operator.
"""

def add_without_plus(num1, num2):
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
    return num1