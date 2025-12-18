"""
QUESTION:
Write a function `get_kth_prime_factor(n, k)` that takes two positive integers `n` and `k` as input and returns the kth prime factor of `n`. A prime factor of an integer `n` is a prime number `p` where `n % p == 0`. If `n` has less than `k` prime factors, return -1. Note that if a prime number divides `n` multiple times, it should be counted multiple times in the list of prime factors. The constraints are `1 <= k <= n <= 1000`.
"""

def get_kth_prime_factor(n, k):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
       factors.append(n)

    if len(factors) < k:
        return -1
    else:
        return factors[k-1]