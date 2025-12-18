"""
QUESTION:
Write a function named `find_lowest_non_prime_sum` that returns the lowest integer that cannot be represented as the sum of two prime numbers. The function should not take any arguments.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_lowest_non_prime_sum():
    """Find the lowest integer that cannot be represented as the sum of two prime numbers."""
    num = 2
    while True:
        is_sum_of_primes = False
        for i in range(2, num):
            if is_prime(i) and is_prime(num - i):
                is_sum_of_primes = True
                break
        if not is_sum_of_primes:
            return num
        num += 1