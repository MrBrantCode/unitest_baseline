"""
QUESTION:
Write a function named `count_primes(n)` to find the count of distinct prime integers less than the given number `n`. The function should use an efficient algorithm and exclude non-prime integers (0 and 1).
"""

def count_primes(n):
    sieve = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: 
            for i in range(x*x, n, x): 
                sieve[i] = False
    return sum(sieve) - 2  # Subtract 2 to not count 0 and 1