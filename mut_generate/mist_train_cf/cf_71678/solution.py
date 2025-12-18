"""
QUESTION:
Write a function `get_factorials_and_prime_factors` that generates the factorial numbers from 1 to n, conducts a prime factorization of each factorial, and returns them in an ordered list of tuples, where each tuple contains the number, its factorial, and the prime factors of the factorial. The function should handle larger input values efficiently.
"""

def get_factorials_and_prime_factors(n):
    def factorial(m): 
        if m == 0: 
            return 1
        else: 
            return m * factorial(m-1)

    def prime_factors(m): 
        i = 2
        factors = []
        while i * i <= m:
            if m % i:
                i += 1
            else:
                m //= i
                factors.append(i)
        if m > 1:
            factors.append(m)
        return factors

    result = []
    for i in range(1, n+1):
        f = factorial(i)
        factors = prime_factors(f)
        result.append((i, f, factors))
    return result