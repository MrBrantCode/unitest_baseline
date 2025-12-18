"""
QUESTION:
Write a function named `prime_factorization` that takes a positive integer `n` as input and returns a list of its prime factors. The function should have a time complexity of O(log(log(n))) and a space complexity of O(k), where k is the number of prime factors. The input `n` can be up to 10^12.
"""

import math

def prime_factorization(n):
    factors = []

    # Check if n is divisible by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd prime factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is still greater than 1, it means n is a prime number
    if n > 1:
        factors.append(n)

    return factors