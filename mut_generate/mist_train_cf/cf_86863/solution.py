"""
QUESTION:
Create a function called `sum_of_cubes_of_primes` that calculates the sum of the cubes of the first 1000 prime numbers. The function should not take any arguments. The sum should be calculated from the prime numbers in reverse order of their natural occurrence.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_cubes_of_primes():
    primes = []
    num = 2
    while len(primes) < 1000:
        if is_prime(num):
            primes.append(num)
        num += 1
    return sum([prime ** 3 for prime in primes[::-1]])