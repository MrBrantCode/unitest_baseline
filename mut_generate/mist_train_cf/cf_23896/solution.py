"""
QUESTION:
Write a function named `add_numbers` that takes two integers as input and returns their sum without using the '+' operator. The function should use bitwise operations to achieve the addition.
"""

def add_numbers(num1, num2):
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
    return num1