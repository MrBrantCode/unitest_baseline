"""
QUESTION:
Implement a function `sum_primes(n)` that calculates the sum of all prime numbers up to a given number `n`. The function should not use any built-in Python functions or libraries that directly calculate prime numbers and should have a time complexity of O(n log log n) or better.
"""

def sum_primes(n):
    if n <= 1:
        return 0
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1
    return sum(i for i in range(2, n+1) if is_prime[i])