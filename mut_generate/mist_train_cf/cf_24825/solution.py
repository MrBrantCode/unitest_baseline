"""
QUESTION:
Write a function called `bitwise_sum` that takes two integers as input and returns their sum without using the "+" operator. Use bitwise operators to achieve this. The function should not have any restrictions on the input values.
"""

def bitwise_sum(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x