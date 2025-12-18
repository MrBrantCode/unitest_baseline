"""
QUESTION:
Create a function `prime_factorize(n)` that takes a positive integer `n` as input and returns a list of its prime factors. The function should decompose the given number into its prime factors. Note that the input number `n` can be any positive integer.
"""

def prime_factorize(n):
    """
    Decompose a positive integer into its prime factors.

    Args:
    n (int): A positive integer.

    Returns:
    list: A list of prime factors of the input number.
    """
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    return prime_factors