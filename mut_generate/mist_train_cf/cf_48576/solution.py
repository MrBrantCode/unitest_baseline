"""
QUESTION:
Implement a function named `is_prime` that checks whether a given number is prime. Using this function, count the quantity of unique prime numbers below 100 and print each of these primes in ascending order without using any built-in prime testing functions.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True