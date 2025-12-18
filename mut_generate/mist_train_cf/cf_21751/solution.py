"""
QUESTION:
Write a function named `lcm_prime_factorization` that takes two integers as input and returns their least common multiple using prime factorization. The function should handle cases where one or both of the input numbers are negative.
"""

def lcm_prime_factorization(num1, num2):
    def prime_factors(n):
        i = 2
        factors = {}
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors[i] = factors.get(i, 0) + 1
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
        return factors

    def lcm(factors1, factors2):
        common_factors = set(list(factors1.keys()) + list(factors2.keys()))
        result = 1
        for factor in common_factors:
            result *= factor ** max(factors1.get(factor, 0), factors2.get(factor, 0))
        return result

    num1, num2 = abs(num1), abs(num2)
    factors1 = prime_factors(num1)
    factors2 = prime_factors(num2)
    return lcm(factors1, factors2)