"""
QUESTION:
Write a function `find_primes(start, end)` that takes two integers `start` and `end` as input, and returns a list of all prime numbers between `start` and `end` (inclusive). The time complexity of the function should be O((end-start+1)*sqrt(end)).
"""

import math

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        if num == 2:
            primes.append(num)
            continue
        if num % 2 == 0:
            continue
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes