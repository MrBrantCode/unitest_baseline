"""
QUESTION:
problem

One day, Sosusa, who loves prime numbers, was playing with the pair $ (p, q) $, where $ p + q $ is a prime number. Suddenly, Sosusa wondered how many of these pairs were prime numbers with $ p $ and $ q $ both less than or equal to $ N $. Find the number on your behalf.



output

Output the number of pairs. Also, output a line break at the end.

Example

Input

3


Output

2
"""

import math

def count_prime_pairs(N):
    # Sieve of Eratosthenes to find all primes up to N+2
    P = [True for _ in range(N + 3)]
    P[0] = P[1] = False
    
    for i in range(2, int(math.sqrt(N + 3)) + 1):
        if P[i]:
            for j in range(i * 2, N + 3, i):
                P[j] = False
    
    count = 0
    for q in range(3, N + 1):
        if P[q] and P[2 + q]:
            count += 2
    
    return count