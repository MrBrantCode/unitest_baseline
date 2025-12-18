"""
QUESTION:
Write a function `is_prime` to determine if a number is prime and use it to calculate the sum of all prime numbers up to and including a given number (in this case, 100). The function should return a boolean value for the primality test and the sum of primes should be calculated based on this test.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True