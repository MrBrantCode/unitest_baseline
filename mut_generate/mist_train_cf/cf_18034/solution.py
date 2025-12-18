"""
QUESTION:
Write a function `generate_fibonacci_primes(n)` that generates a list of the first `n` prime numbers that are also Fibonacci numbers. The function should use the Sieve of Eratosthenes algorithm to find prime numbers efficiently. The list of Fibonacci numbers should be generated on the fly without a predefined limit.
"""

def generate_fibonacci_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fibonacci_primes = []
    a, b = 0, 1
    while len(fibonacci_primes) < n:
        a, b = b, a + b
        if is_prime(b):
            fibonacci_primes.append(b)

    return fibonacci_primes