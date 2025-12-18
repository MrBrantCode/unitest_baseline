"""
QUESTION:
Write a function `generate_prime_numbers(n)` that generates a list of all prime numbers in the range from 0 to the given number `n`, excluding any prime numbers that contain the digit 5. The function should return a list of integers.
"""

import math

def generate_prime_numbers(n):
    primes = []
    for num in range(n + 1):
        if '5' not in str(num):
            if num > 1:
                is_prime = True
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
    return primes