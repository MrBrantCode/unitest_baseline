"""
QUESTION:
Write a function `sum_of_primes(n)` to compute the sum of all prime numbers from 2 to `n`. The function should have a time complexity of O(sqrt(n)) and use a constant amount of additional space.
"""

import math

def sum_of_primes(n):
    isPrime = [True] * (n+1)
    isPrime[0] = isPrime[1] = False
    sum = 0
    
    for i in range(2, int(math.sqrt(n))+1):
        if isPrime[i]:
            for j in range(i*i, n+1, i):
                isPrime[j] = False
    
    for i in range(2, n+1):
        if isPrime[i]:
            sum += i
    
    return sum