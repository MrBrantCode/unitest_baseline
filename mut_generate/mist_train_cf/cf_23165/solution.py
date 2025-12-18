"""
QUESTION:
Write a function `find_primes(n: int) -> List[int]` that returns an array with all the prime numbers between 2 and `n`, inclusive. The input parameter `n` is a positive integer, where 2 <= n <= 10^9. The solution should be optimized for performance with a time complexity of O(n*log(log(n))) or better, without using any external libraries or built-in functions for checking prime numbers.
"""

from typing import List

def find_primes(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    # Iterate up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, n + 1) if sieve[i]]