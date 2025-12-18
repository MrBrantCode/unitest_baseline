"""
QUESTION:
Write a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function should work for both positive and negative integers, and it should be efficient for large inputs. The input `n` is guaranteed to be a non-zero integer.
"""

def largest_prime_factor(n):
    """
    This function takes an integer n as input and returns its largest prime factor.

    Args:
        n (int): A non-zero integer.

    Returns:
        int: The largest prime factor of n.
    """
    n = abs(n)
    i = 2

    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i

    return n