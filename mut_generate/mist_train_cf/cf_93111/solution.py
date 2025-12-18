"""
QUESTION:
Implement a function named `gcd` that takes two integers `a` and `b` as parameters and returns their greatest common divisor without using any built-in library or function. The function should be efficient for large numbers.
"""

def gcd(a, b):
    # Make sure a is always the larger number
    if a < b:
        a, b = b, a

    while b != 0:
        # Calculate the remainder of a divided by b
        remainder = a % b

        # Set a to b and b to the remainder
        a = b
        b = remainder

    return a