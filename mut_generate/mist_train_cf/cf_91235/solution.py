"""
QUESTION:
Implement the function "add_two_numbers" that takes two integers as input and returns their sum without using the "+" operator or any built-in functions for addition. The function should only use bitwise operators.
"""

def add_two_numbers(a, b):
    # Iterate until there is no carry left
    while b != 0:
        # Calculate the carry (using bitwise AND)
        carry = a & b

        # Calculate the sum without carry (using bitwise XOR)
        a = a ^ b

        # Shift the carry by one bit (using bitwise left shift)
        b = carry << 1

    return a