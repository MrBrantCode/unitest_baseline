"""
QUESTION:
Write a function named `print_primes` that takes two parameters, `start` and `end`, representing a range of numbers. This function should print all prime numbers within the given range (inclusive). A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    for i in range(start, end + 1):
        if is_prime(i):
            print(i)