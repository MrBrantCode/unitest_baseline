"""
QUESTION:
Write a program that includes a function named `is_prime` to check if a number is prime and another function named `generate_primes` to generate prime numbers up to a given number `n`. The `is_prime` function should have a time complexity of O(√n) and the `generate_primes` function should have a time complexity of O(n log(log n)) and space complexity of O(1). You cannot use any built-in functions or libraries for generating prime numbers or checking primality.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    if n < 2:
        return
    print(2)
    for num in range(3, n + 1, 2):
        if is_prime(num):
            print(num)