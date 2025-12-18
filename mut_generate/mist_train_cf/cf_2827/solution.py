"""
QUESTION:
Write a function `is_prime(n)` to check if a number `n` is prime or not. Using this function, calculate the sum of all prime numbers from 0 to 1,000,000 and return the sum. The input `n` in the function `is_prime(n)` will be a non-negative integer and the output will be a boolean value. The range of numbers for which the sum of primes needs to be calculated is from 2 to 1,000,000 (inclusive).
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True