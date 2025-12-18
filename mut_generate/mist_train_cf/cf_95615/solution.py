"""
QUESTION:
Write a function called `bitwise_addition` that takes in two integers `a` and `b` as input and returns the result of adding `a` and `b` together using only bitwise operations such as `&`, `|`, `^`, `<<`, `>>`, and `~`. The function should not use any arithmetic operators (+, -, *, /) or the `+` operator.
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