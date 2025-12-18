"""
QUESTION:
Write a function named `largest_prime_factor` that takes an integer `n` as input, where `abs(n) > 1` and `n` is not prime. The function should return the largest prime factor of `n`. The function should work correctly for both positive and negative input numbers, and it should efficiently find the prime factors by minimizing the number of divisions.
"""

def largest_prime_factor(n: int):
    n = abs(n)
    max_prime = -1
    while n % 2 == 0:
        n >>= 1
        max_prime = 2
        
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
            
    if n > 2:
        max_prime = n
        
    return max_prime