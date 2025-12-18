"""
QUESTION:
Write a function `bitwise_addition` that takes two integers `a` and `b` as input. The function should use only bitwise operations (`&`, `|`, `^`, `<<`, `>>`, `~`) to add `a` and `b` together and return the result without using any arithmetic operators (`+`, `-`, `*`, `/`) or the `+` operator.
"""

def bitwise_addition(a, b):
    # Iterate until there is no carry left
    while b != 0:
        # Calculate the carry using AND operator
        carry = a & b

        # XOR the bits to get the sum
        a = a ^ b

        # Left shift the carry by 1 to add to the next bit
        b = carry << 1

    return a