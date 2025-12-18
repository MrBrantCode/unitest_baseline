"""
QUESTION:
Write a function named `add_numbers` that takes two integers as input and returns their sum without using any arithmetic operators or built-in functions specifically designed for addition. The function should utilize bitwise operations to achieve this.
"""

def add_numbers(a, b):
    while b != 0:
        # Calculate the carry
        carry = a & b

        # Sum the bits without considering the carry
        a = a ^ b

        # Left shift the carry to be added in the next iteration
        b = carry << 1

    return a