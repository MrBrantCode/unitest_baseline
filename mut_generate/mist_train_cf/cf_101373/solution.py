"""
QUESTION:
Write a function `sum_of_squares_of_prime_factors` that takes an integer `n` as input and returns the sum of the squares of its prime factors.
"""

def sum_of_squares_of_prime_factors(n):
    """
    Calculates the sum of the squares of the prime factors of n.
    """
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    primes = set()
    for factor in factors:
        for i in range(2, int(factor ** 0.5) + 1):
            if (factor % i) == 0:
                break
        else:
            primes.add(factor)
    return sum(p ** 2 for p in primes)