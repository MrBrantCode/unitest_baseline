"""
QUESTION:
Write a function `stats_prime_nums(n)` that calculates the sum, average, median, and standard deviation of the first n prime numbers. The function should take an integer `n` as input and handle edge cases where `n` is less than 1 or a non-integer. The function should return the sum, average, median, and standard deviation of the first `n` prime numbers.
"""

import numpy as np

def stats_prime_nums(n):
    if not isinstance(n, int) or n < 1:
        return "n should be a positive integer."
    
    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, int(np.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True
    
    prime_nums = []
    i = 2
    while len(prime_nums) < n:
        if is_prime(i):
            prime_nums.append(i)
        i += 1
    
    sum_of_primes = np.sum(prime_nums)
    avg_primes = np.mean(prime_nums)
    median_primes = np.median(prime_nums)
    std_primes = np.std(prime_nums)
    
    return sum_of_primes, avg_primes, median_primes, std_primes