"""
QUESTION:
Write a function named `count_same_prime_factors(n)` that takes an integer `n` as input, where `n` is the upper limit of the range of integers to consider. The function should return the number of integers `i` in the range `1 < i < n` such that `i` and `i + 2` have the same number of prime factors.
"""

def count_same_prime_factors(n):
    prime_fac_count = [0] * (n + 1)
    for i in range(2, n+1):
        if prime_fac_count[i] == 0:
            for j in range(i, n+1, i):
                prime_fac_count[j] += 1
    count = 0
    for i in range(2, n-1):
        if prime_fac_count[i] == prime_fac_count[i+2]:
            count += 1
    return count