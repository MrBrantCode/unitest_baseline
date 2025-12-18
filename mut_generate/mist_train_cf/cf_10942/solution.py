"""
QUESTION:
Write a function named `sum_primes` that calculates the sum of all prime numbers between 1 and n. The function should take an integer `n` as input and return the sum of prime numbers up to `n`. The function should use a list comprehension and should not include the number `n` itself if it is not a prime number.
"""

def sum_primes(n):
    """
    Calculate the sum of all prime numbers between 1 and n.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The sum of prime numbers up to n.
    """
    return sum([num for num in range(2, n) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))])