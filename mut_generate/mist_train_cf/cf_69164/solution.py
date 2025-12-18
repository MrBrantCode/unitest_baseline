"""
QUESTION:
Write a function `check_prime(n)` that takes a positive integer `n` as input and returns "prime" if `n` is a prime number, otherwise returns "composite". Assume the input `n` will be validated to ensure it is a positive integer before calling the function.
"""

def check_prime(n):
    """
    This function determines whether a number is prime or composite.

    Args:
    n (int): A positive integer.

    Returns:
    str: 'prime' if the number is prime, 'composite' otherwise.
    """

    if n <= 1:
        return 'composite'
    elif n <= 3:
        return 'prime'
    elif n % 2 == 0 or n % 3 == 0:
        return 'composite'
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 'composite'
        i += 6
    return 'prime'