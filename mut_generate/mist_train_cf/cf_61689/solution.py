"""
QUESTION:
Write a function `generate_primes(n)` that returns a list of the first 'n' prime numbers. The function should validate if 'n' is a positive integer and handle any exceptions. The function should also include a helper function `is_prime(num)` to determine whether a number is a prime number.
"""

def is_prime(num):
    """
    This function determines whether a number is a prime number.
    """
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def generate_primes(n):
    """
    This function generates the first 'n' prime numbers.
    """
    if not isinstance(n, int) or n < 1:
        raise Exception("The input must be a positive integer!")
    primes = [i for i in range(2, n*10) if is_prime(i)]
    return primes[:n]