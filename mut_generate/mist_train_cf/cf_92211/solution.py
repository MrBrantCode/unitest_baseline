"""
QUESTION:
Write a function `find_prime_numbers(n)` to return all prime numbers less than a given positive integer `n` where `n > 1`. The function should use the Sieve of Eratosthenes algorithm and return a list of prime numbers.
"""

def find_prime_numbers(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1

    primes = [i for i in range(2, n+1) if is_prime[i]]
    return primes