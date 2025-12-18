"""
QUESTION:
Write a function named `find_primes_in_range` that takes two integers, `start` and `end`, representing a range of numbers. The function should find all prime numbers within the given range (inclusive) without using any built-in prime checking functions or libraries. It should then return the sum of these prime numbers. Assume that `start` and `end` are valid integers and `start` is not greater than `end`.
"""

import math

def find_primes_in_range(start, end):
    isPrime = [True] * (end + 1)
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(math.sqrt(end)) + 1):
        if isPrime[i]:
            for j in range(i * i, end + 1, i):
                isPrime[j] = False

    prime_sum = 0
    for i in range(start, end + 1):
        if isPrime[i]:
            prime_sum += i

    return prime_sum