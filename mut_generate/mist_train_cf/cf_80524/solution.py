"""
QUESTION:
Create a function `count_primes(n, m)` that calculates the number of prime numbers within the specified range from `n` to `m`. The function should be optimized for efficiency by checking for divisors up to the square root of a number.
"""

import math

def count_primes(n, m):
    count = 0
    for num in range(n, m+1):
        if num > 1:
           for i in range(2, int(math.sqrt(num))+1):
               if (num % i) == 0:
                   break
           else:
               count += 1
    return count