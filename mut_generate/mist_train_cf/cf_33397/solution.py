"""
QUESTION:
Write a function named `prime_factors` that takes a positive integer `n` as input and returns a list of its prime factors in ascending order. The function should be efficient enough to handle large numbers.
"""

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors