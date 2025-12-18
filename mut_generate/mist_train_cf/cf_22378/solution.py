"""
QUESTION:
Write a function `gcd` that takes two integers as input and returns their greatest common divisor without using the built-in gcd function or any mathematical libraries.
"""

def gcd(a, b):
    """
    This function calculates the greatest common divisor of two integers using the Euclidean algorithm.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.
    """

    while b != 0:
        # In each iteration, replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    
    # When 'b' becomes zero, 'a' will be the GCD
    return a