"""
QUESTION:
Create a function `generate_primes(n)` that generates an array of 'n' integers, where each element is a prime number. The function should return the array of prime numbers.
"""

def generate_primes(n):
    """
    Generate an array of 'n' prime numbers.

    Args:
    n (int): The number of prime numbers to generate.

    Returns:
    list: A list of 'n' prime numbers.
    """
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes