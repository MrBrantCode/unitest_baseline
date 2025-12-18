"""
QUESTION:
Create a function named `is_prime(n)` that checks whether a given number `n` is a prime number using the Sieve of Eratosthenes algorithm. If `n` is not a prime number, the function should return the smallest prime factor of `n`. The function should be able to handle numbers up to 10^9 efficiently. The time complexity should be O(n log log n) and the space complexity should be O(n).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    if is_prime[n]:
        return True
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0 and is_prime[i]:
            return i
    
    return False