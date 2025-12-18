"""
QUESTION:
Generate a sequence of the first `n` Fibonacci numbers that are prime. The function should be named `fibonacci_primes(n)` and should return a list of prime Fibonacci numbers. The function should use another helper function `is_prime(n)` to check if a number is prime or not.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_primes(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        if is_prime(b):
            sequence.append(b)
        a, b = b, a + b
    return sequence