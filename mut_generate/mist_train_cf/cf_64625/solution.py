"""
QUESTION:
Write a function named `add_two_numbers` that takes two integers `x` and `y` as parameters and returns their sum without using any arithmetic operators. The function should use bit manipulation operations.
"""

def add_two_numbers(x, y):
    # loop till there is no carry left
    while (y != 0):
        # carry contains common set bits of x and y
        carry = x & y

        # Sum of bits of x and y where at least one of the bits is not set
        x = x ^ y

        # carry is shifted by one so that adding it to x gives the required sum
        y = carry << 1

    return x