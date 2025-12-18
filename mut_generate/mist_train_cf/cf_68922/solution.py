"""
QUESTION:
Develop a function `get_prime_factors(n)` that takes an integer `n` not exceeding 10^12 as input and returns all prime divisors of `n`. The function should be optimized for time complexity, considering the given upper limit of input, and handle potential errors or exceptions.
"""

import math

def get_prime_factors(n):
    """
    This function takes an integer n not exceeding 10^12 as input and returns all prime divisors of n.

    Args:
        n (int): The input number.

    Returns:
        list: A list of prime factors of n.
    """
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            prime_factors.append(i)
            n = n / i
    if n > 2:
        prime_factors.append(n)
    return prime_factors