"""
QUESTION:
Create a function named `sum_of_primes` that calculates the sum of prime numbers within a given range defined by the parameters `lower_bound` and `upper_bound`, where the range can be as large as 10^9. The function should be efficient and return the sum of prime numbers between `lower_bound` and `upper_bound` (inclusive).
"""

import math

def sum_of_primes(lower_bound, upper_bound):
    is_prime = [True] * (upper_bound + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(upper_bound)) + 1):
        if is_prime[i]:
            for j in range(i * i, upper_bound + 1, i):
                is_prime[j] = False
    prime_sum = 0
    for i in range(lower_bound, upper_bound + 1):
        if is_prime[i]:
            prime_sum += i
    return prime_sum