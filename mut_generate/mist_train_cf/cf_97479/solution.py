"""
QUESTION:
Implement a function `add_numbers(num1, num2)` that calculates the sum of two integers without using the addition operator (+) or any built-in functions that directly perform addition.
"""

def add_numbers(num1, num2):
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
    return num1