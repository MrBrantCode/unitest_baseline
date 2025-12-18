"""
QUESTION:
Implement a function named `sum_without_plus` that takes two integers `x` and `y` as input and returns their sum without using the '+' operator. The function should have a time complexity of O(log n), where n is the value of the larger integer.
"""

def sum_without_plus(x, y):
    # Iterate until there are no more bits to carry
    while y != 0:
        # Carry contains the common set bits of x and y
        carry = x & y

        # Sum of bits of x and y without considering the carry
        x = x ^ y

        # Carry is shifted by one so that adding it to x gives the required sum
        y = carry << 1

    return x