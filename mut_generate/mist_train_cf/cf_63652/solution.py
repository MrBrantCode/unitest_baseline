"""
QUESTION:
Write a function named `fast_s(n)` that calculates the sum of `f(r)` for all divisors of `n` where `f(r)` is an approximation of the count of distinct Pythagorean lattice grid quadrilaterals for which the radius of the circumcircle is `r`. The function should return the sum `S(n)` as an integer. The input `n` is a positive integer.
"""

import itertools

def fast_s(n):
    # Returns the prime factorization of n
    def factorize(n):
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

    # Returns all divisors of n
    def get_divisors(n):
        factors = factorize(n)
        product = [1]
        for i in factors:
            product = product + [x*i for x in product]
        return sorted(list(set(product)))

    # Returns f(r) based on approximations
    def f_approx(r):
        return int((3.208 * r - 36.97) * r + 190)

    # Returns S(n), computed as a sum of f(r) for all divisors of n
    divisors = get_divisors(n)
    return sum(f_approx(r) for r in divisors if r*r<=n)