"""
QUESTION:
Write a function `largest_prime_factor(n: int)` that returns the largest prime factor of a given integer `n`, where `n` can be either positive or negative, `abs(n) > 1`, and `n` is not prime. The function should efficiently find the prime factors of `n`.
"""

def largest_prime_factor(n: int):
    def is_prime(num: int):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = abs(n)

    largest_prime = -1
    for i in range(2, n+1):
        while n % i == 0 and is_prime(i):
            largest_prime = i
            n //= i
        if n == 1:
            break
    return largest_prime