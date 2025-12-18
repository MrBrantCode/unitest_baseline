"""
QUESTION:
Write a function `count_digit_only_prime_divisors(n)` that takes an integer `n` as input and returns the total number of digit only divisors of `n` that are also prime numbers. A digit only number is a number that has only digits in its digits (no special characters, decimal points, etc.), i.e., a positive integer. The function should be efficient for small values of `n`.
"""

import math

def is_digit_only(num):
    # Check if a number is digit only
    for char in str(num):
        if char < '0' or char > '9':
            return False
    return True

def is_prime(num):
    # Check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def count_digit_only_prime_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and is_digit_only(i) and is_prime(i):
            count += 1
    return count