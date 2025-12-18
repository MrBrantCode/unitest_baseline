"""
QUESTION:
Write a function that calculates the largest prime factor of a given number and returns a list of all the prime factors in ascending order. The function should be able to handle numbers up to 10^5 in under one second.
"""

def entrance(n):
    def prime_factors(num):
        i = 2
        factors = []
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        return factors

    return prime_factors(n)

# alternative approach using Sieve of Eratosthenes
def entrance(n):
    def prime_factorization_upto_n(max_n):
        factorizations = [ [] for _ in range(max_n+1) ]
        for i in range(2, max_n+1):
            if factorizations[i]: continue
            for j in range(i, max_n+1, i):
                factor = i
                n = j
                while n % factor == 0:
                    factorizations[j].append(factor)
                    n //= factor
        return factorizations

    factorizations = prime_factorization_upto_n(n)
    return factorizations[n]