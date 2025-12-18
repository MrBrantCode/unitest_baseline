"""
QUESTION:
Write a function called `generate_prime_numbers` that takes an integer `n` as input and returns the first `n` prime numbers. Implement a helper function `is_prime` that checks if a given number is a prime number. The `is_prime` function should return `True` if the number is prime and `False` otherwise. The generated prime numbers should be efficient for large values of `n`. The `is_prime` function should not use any built-in functions or libraries that directly solve the prime number problem.
"""

def is_prime(num):
    """Check if a given number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_numbers(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes