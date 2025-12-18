"""
QUESTION:
Design a function `bitwise_sum(a, b)` that calculates the sum of two numbers using only bitwise operations, without the arithmetic operators + and -. The function should handle both negative and positive integers within the range of a 32-bit signed integer and return their sum.
"""

def bitwise_sum(a, b):
    # Iterate until there is no carry left
    while b != 0:
        # Calculate the carry
        carry = a & b

        # Calculate the sum without considering the carry
        a = a ^ b

        # Shift the carry to the left by 1 position
        b = carry << 1

    return a