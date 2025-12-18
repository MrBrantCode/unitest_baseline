"""
QUESTION:
Write a function named `generate_array(n, m)` that generates an array of increasing numbers starting from 1 and ending at a number `m`, where each number in the array must be divisible by a prime number less than or equal to `n`, and `m` is a positive integer greater than or equal to the number of elements in the resulting array.
"""

import math

def generate_array(n, m):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    
    result = []
    i = 1
    while len(result) < m:
        divisible_by_prime = False
        for prime in primes:
            if i % prime == 0:
                divisible_by_prime = True
                break
        if divisible_by_prime:
            result.append(i)
        i += 1
    
    return result