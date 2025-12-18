"""
QUESTION:
Write a function `generate_primes` that takes an integer `upper_limit` as input and prints all prime numbers up to `upper_limit` along with their type, which can be regular, Eisenstein with no imaginary part, or Gaussian. A regular prime is a natural number greater than 1 that has only two positive divisors: 1 and the number itself. An Eisenstein prime with no imaginary part is a prime number of the form 3n - 1, where n is a natural number. A Gaussian prime is a complex number a + bi, where a and b are integers and either the number is a regular prime and not of the form 4n+3, where n is a natural number, or the number is of the form a + bi (where b ≠ 0) and a^2 + b^2 is prime.
"""

import math

def generate_primes(upper_limit):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(math.sqrt(n)) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    def is_eisenstein_prime(n):
        if is_prime(n) and n % 3 == 2:
            return True
        return False

    def is_gaussian_prime(n):
        if is_prime(n) and n % 4 != 3:
            return True
        return False

    for n in range(upper_limit+1):
        if is_prime(n):
            print(f"Regular prime: {n}")
        if is_eisenstein_prime(n):
            print(f"Eisenstein prime with no imaginary part: {n}")
        if is_gaussian_prime(n):
            print(f"Gaussian prime: {n}")