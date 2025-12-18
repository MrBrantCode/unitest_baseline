"""
QUESTION:
Write a function named `prime_factors` that takes an integer `n` as input, where `1 <= n <= 10^5` and `n` is not a prime number. The function should return a list of prime factors of `n` in descending order.
"""

def prime_factors(n):
    """
    This function takes an integer n as input and returns a list of prime factors of n in descending order.

    Args:
    n (int): The input number.

    Returns:
    list: A list of prime factors of n in descending order.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return sorted(factors, reverse=True)