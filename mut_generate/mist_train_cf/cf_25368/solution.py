"""
QUESTION:
Write a function named `find_lcm` that takes two positive integers `a` and `b` as input and returns their least common multiple. The function should not take any other arguments and should not use any built-in functions to calculate the LCM or GCD. The function should implement the Euclidean algorithm to find the GCD.
"""

def find_lcm(a, b):
    """
    Calculate the least common multiple of two positive integers.

    Args:
        a (int): The first positive integer.
        b (int): The second positive integer.

    Returns:
        int: The least common multiple of a and b.
    """

    # Define a helper function to calculate the GCD using the Euclidean algorithm
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # Calculate the LCM by dividing the product of a and b by their GCD
    return a * b // gcd(a, b)