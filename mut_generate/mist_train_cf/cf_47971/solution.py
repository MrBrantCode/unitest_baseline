"""
QUESTION:
Write a function `greatest_prime_factor(n)` that takes an integer `n` as input and returns the greatest prime factor of `n`. The function should be efficient enough to handle large numbers.
"""

def greatest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n