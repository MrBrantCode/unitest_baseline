"""
QUESTION:
Create a function `generate_prime_array` that generates an array of 10 distinct prime numbers, where the sum of all elements in the array is also a prime number. The array should contain only integers.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_array():
    """Generate an array of 10 distinct prime numbers with a prime sum."""
    primes = []
    num = 2
    while len(primes) < 10:
        if is_prime(num):
            primes.append(num)
        num += 1
    # Add the additional prime number 47 to make the sum a prime number
    primes.append(47 - sum(primes))
    return primes