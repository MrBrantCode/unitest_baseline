"""
QUESTION:
Create a function named `first_primes` to generate the first 'n' prime numbers. This function should utilize another helper function named `is_prime` that checks if a number is prime. Implement the prime number generation using a do-while loop or a while loop. The function should return a list of the first 'n' prime numbers.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def first_primes(n):
    """Generate the first 'n' prime numbers."""
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes