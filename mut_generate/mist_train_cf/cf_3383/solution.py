"""
QUESTION:
Implement a function named `sum_of_primes` that takes an integer `n` as input, calculates the sum of all prime numbers up to `n` using a segmented sieve algorithm, and returns the result. The function must have a time complexity of O(n^(3/2)), handle large values of `n` efficiently, and output the result in a human-readable format. The input `n` must be a non-negative integer.
"""

import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate prime numbers up to n using segmented sieve algorithm
def segmented_sieve(n):
    limit = int(math.sqrt(n)) + 1
    prime = [True] * limit
    primes = []
    for p in range(2, limit):
        if prime[p]:
            primes.append(p)
            for i in range(p * p, limit, p):
                prime[i] = False
    return primes

# Function to calculate the sum of prime numbers up to n using segmented sieve algorithm
def sum_of_primes(n):
    if n < 0:
        return "Invalid input: n must be a positive integer."
    
    primes = segmented_sieve(n)
    total_sum = sum(num for num in range(2, n + 1) if is_prime(num) or num in primes)
    
    return total_sum