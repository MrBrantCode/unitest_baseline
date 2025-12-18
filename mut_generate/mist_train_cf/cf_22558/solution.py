"""
QUESTION:
Write a function `generate_array(n, m)` that generates an array of increasing numbers starting from 1 and ending at m, where each number in the array is divisible by a prime number less than or equal to n. The function should take two parameters: n, a positive integer representing the upper limit for prime numbers, and m, a positive integer representing the desired length of the output array. The function should return an array of m numbers.
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