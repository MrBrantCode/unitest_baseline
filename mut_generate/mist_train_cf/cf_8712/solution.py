"""
QUESTION:
Implement the function sum_of_primes(N) that calculates the sum of all prime numbers within a given range of integers from 1 to N with a time complexity of O(N log log N) for finding the prime numbers.
"""

import math

def sum_of_primes(N):
    # Initialize a boolean array to mark all numbers as prime
    is_prime = [True] * (N+1)
    is_prime[0] = is_prime[1] = False

    # Loop through all numbers up to square root of N
    for i in range(2, int(math.sqrt(N))+1):
        if is_prime[i]:
            # Mark all multiples of i as non-prime
            for j in range(i*i, N+1, i):
                is_prime[j] = False

    # Calculate the sum of all prime numbers
    prime_sum = 0
    for i in range(2, N+1):
        if is_prime[i]:
            prime_sum += i

    return prime_sum