"""
QUESTION:
Write a function called `compute_variance_of_primes` that generates the first `n` unique prime numbers and returns their variance. The function should take an integer `n` as input and return a float value representing the variance of the generated prime numbers.
"""

import numpy as np

def compute_variance_of_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        max_div = int(np.floor(np.sqrt(num)))
        for i in range(3, 1 + max_div, 2):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return np.var(primes)