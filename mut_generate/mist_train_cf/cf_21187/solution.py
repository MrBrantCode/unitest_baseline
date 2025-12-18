"""
QUESTION:
Create a function `get_prime_numbers` that takes in an integer `n` as input and returns a list containing the first `n` prime numbers. The function should use a recursive function `is_prime` to check if a number is prime using the trial division method, which checks if a number is divisible by any number less than its square root (excluding 1 and itself). The function should continue generating prime numbers until the desired number `n` of primes is reached.
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