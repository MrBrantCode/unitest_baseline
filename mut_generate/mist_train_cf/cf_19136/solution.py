"""
QUESTION:
Create a function called `generate_primes` that generates the first n prime numbers. The function should take an integer n as input and return a list of integers. The generated prime numbers should be in ascending order. The function should be efficient enough to generate at least the first 10,000 prime numbers.
"""

def generate_primes(n):
    return [x for x in range(2, n*10) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))][:n]