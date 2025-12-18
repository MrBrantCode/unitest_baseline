"""
QUESTION:
Implement the function `sum_and_product(a, b, c)` that takes three integers as arguments and returns a tuple of two values. The first value in the tuple is the sum of `a` and `b` without using the arithmetic operators `+` and `-`. The second value in the tuple is the product of the sum and `c` without using the operator `*`. The function should work for integers in the range `-1000 <= a, b, c <= 1000`.
"""

def sum_and_product(a, b, c):
    """
    This function calculates the sum of a and b without using the arithmetic operators + and -, 
    and the product of the sum and c without using the operator *.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        tuple: A tuple containing the sum of a and b, and the product of the sum and c.
    """

    # Calculate the sum of a and b without using + and -
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    # Calculate the product of the sum and c without using *
    result = 0
    i = 0
    while c > 0:
        if c & 1:
            result += a << i
        c >>= 1
        i += 1

    return a, result