"""
QUESTION:
Write a function called `generate_primes` to generate the first N prime numbers. The function should take an integer N as input and return a list of the first N prime numbers.
"""

def generate_primes(n):
    """
    Generate the first N prime numbers.

    Args:
    n (int): The number of prime numbers to generate.

    Returns:
    list: A list of the first N prime numbers.
    """
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % p > 0 for p in primes):
            primes.append(num)
        num += 1
    return primes