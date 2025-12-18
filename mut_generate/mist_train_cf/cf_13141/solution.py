"""
QUESTION:
Create a function `lcm` that calculates the least common multiple of three integers `a`, `b`, and `c` using prime factorization. The function should return the LCM as an integer. The function should not use any built-in functions or libraries to calculate the prime factors or the LCM.
"""

def lcm(a, b, c):
    def prime_factors(n):
        factors = []
        for prime in range(2, int(n**0.5) + 1):
            while n % prime == 0:
                factors.append(prime)
                n //= prime
        if n > 1:
            factors.append(n)
        return factors

    def get_unique_prime_factors(a, b, c):
        unique_factors = set(a + b + c)
        return list(unique_factors)

    def count_occurrence(prime_factor, prime_factors):
        return prime_factors.count(prime_factor)

    prime_factors_a = prime_factors(a)
    prime_factors_b = prime_factors(b)
    prime_factors_c = prime_factors(c)

    unique_prime_factors = get_unique_prime_factors(prime_factors_a, prime_factors_b, prime_factors_c)

    result = 1
    for prime_factor in unique_prime_factors:
        highest_occurrence = max(count_occurrence(prime_factor, prime_factors_a), 
                                 count_occurrence(prime_factor, prime_factors_b), 
                                 count_occurrence(prime_factor, prime_factors_c))
        result *= (prime_factor ** highest_occurrence)

    return result