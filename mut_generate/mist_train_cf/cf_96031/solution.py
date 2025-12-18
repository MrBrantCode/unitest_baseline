"""
QUESTION:
Create a function called `primes_up_to_n(n)` that generates a list of prime numbers from 2 to `n`. The input `n` can be up to 10^9, and the function should have a time complexity of O(sqrt(n)).
"""

import math

def primes_up_to_n(n):
    primes = []
    for i in range(2, n+1):
        if i <= 1:
            continue
        if i <= 3:
            primes.append(i)
            continue
        if i % 2 == 0 or i % 3 == 0:
            continue
        for j in range(5, int(math.sqrt(i)) + 1, 6):
            if i % j == 0 or i % (j + 2) == 0:
                break
        else:
            primes.append(i)
    return primes