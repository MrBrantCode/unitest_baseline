"""
QUESTION:
Write a function called `sum_of_primes(n)` that calculates the sum of all prime numbers from 2 to n with a time complexity better than O(n^2). The function should return the sum of prime numbers.
"""

def sum_of_primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    sum_primes = 0
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            sum_primes += p
    return sum_primes