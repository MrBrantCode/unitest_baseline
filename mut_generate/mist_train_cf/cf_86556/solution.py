"""
QUESTION:
Create a function named `generate_prime_numbers(n)` that takes an integer `n` as input and returns a list of the first `n` prime numbers and their sum. The function should have a time complexity of O(n√m) and space complexity of O(n), where `m` is the largest prime number in the list.
"""

import math

def generate_prime_numbers(n):
    primes = []
    is_prime = [True] * (n + 1)
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    prime_sum = sum(primes)

    return primes, prime_sum