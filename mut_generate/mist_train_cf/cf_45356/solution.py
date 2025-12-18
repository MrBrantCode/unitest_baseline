"""
QUESTION:
Write a function named `prime_product_quartet` that takes an integer `a` less than 20,000 as input and returns a tuple of distinct prime factors if `a` can be represented as a product of 2, 3, or 4 unique prime numbers. If `a` cannot be represented in such a way, the function should return 'Not a product of distinct prime numbers.'
"""

def prime_product_quartet(a):
    def check_prime(b):
        for z in range(2, int(b**0.5) + 1):
            if b % z == 0:
                return False
        return True

    def fill_prime_factors(a):
        i = 2
        factors = []
        while i * i <= a:
            if a % i:
                i += 1
            else:
                a //= i
                if check_prime(i) and i not in factors:
                    factors.append(i)
        if a > 1 and check_prime(a) and a not in factors:
            factors.append(a)
        return factors

    factors = fill_prime_factors(a)
    if 2 <= len(factors) <= 4:
        return tuple(factors)
    else:
        return 'Not a product of distinct prime numbers.'