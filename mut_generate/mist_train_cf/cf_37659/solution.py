"""
QUESTION:
Write a function `primeFactorization` that takes an integer `m` as input, where 1 ≤ `m` ≤ 1,000,000,000, and returns a list of prime factors of `m` in ascending order. The list should contain the prime numbers that multiply together to give the original number `m`.
"""

def primeFactorization(m):
    factors = []
    while m % 2 == 0:
        factors.append(2)
        m = m // 2
    for i in range(3, int(m**0.5) + 1, 2):
        while m % i == 0:
            factors.append(i)
            m = m // i
    if m > 2:
        factors.append(m)
    return factors