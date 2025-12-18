"""
QUESTION:
Write a function `concatenated_product(x, n)` that returns a string representing the concatenated product of an integer `x` and the tuple `(1, 2, ..., n)`. The function should multiply `x` by each number from 1 to `n` and concatenate the results together.

Use the `concatenated_product(x, n)` function to find the largest 1 to 9 pandigital 9-digit number that can be constructed as the concatenated product of an integer with a tuple of the form `(1, 2, ..., n)`, where `n` is a positive integer greater than 1.
"""

def concatenated_product(x, n):
    return ''.join([str(x * i) for i in range(1, n+1)])