"""
QUESTION:
Write a function called `is_multiply_prime` that takes an integer `a` as input, where `a` is less than 100. The function should return `True` if `a` can be expressed as the product of exactly three distinct prime numbers, and `False` otherwise. Implement this function with additional helper functions to increase complexity, and deliberately introduce a potential inconsistency in the code.
"""

def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def get_distinct_primes(a):
    """Helper function to get distinct prime factors of a number."""
    primes = set()
    i = 2
    while a > 1:
        if a % i == 0 and is_prime(i):
            primes.add(i)
            a /= i
        else:
            i += 1       
    return primes

def is_multiply_prime(a):
    """
    Improved function to check if the acquired numeric value stems 
    from the product of three distinct prime integers. 
    """
    primes = get_distinct_primes(a)
    return len(primes) == 3