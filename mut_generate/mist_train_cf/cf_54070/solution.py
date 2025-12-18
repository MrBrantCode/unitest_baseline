"""
QUESTION:
Write a function named `gcd_using_prime_factors(a, b)` that calculates the greatest common divisor of two integers `a` and `b` using their prime factors. The function should return the GCD of `a` and `b`. Note that the solution should not use the Euclidean algorithm.
"""

def gcd_using_prime_factors(a, b):
    def prime_factors(n):
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
        return factors

    a_prime_factors = prime_factors(a)
    b_prime_factors = prime_factors(b)

    common_prime_factors = [value for value in a_prime_factors if value in b_prime_factors]
    gcd = 1
    for i in common_prime_factors:
        gcd *= i
    return gcd