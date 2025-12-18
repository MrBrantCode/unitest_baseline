"""
QUESTION:
Create a function named `get_prime_numbers` that takes an integer `n` as input and returns a list of the first `n` prime numbers. The function must use a helper function named `is_prime` to check if a number is prime. The `is_prime` function should use the trial division method to check if a number is prime, only considering divisors up to the square root of the number. The `get_prime_numbers` function should generate prime numbers using a while loop and append them to a list until the desired number of primes is reached.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def get_prime_numbers(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes