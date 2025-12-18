"""
QUESTION:
Write a function named `fibonacci_prime` that generates a Fibonacci sequence with a given length that only contains prime numbers. The function should take an integer `n` as input, representing the desired length of the Fibonacci sequence, and return a list of the first `n` prime numbers in the Fibonacci sequence.
"""

def fibonacci_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 0, 1
    prime_fib = []
    while len(prime_fib) < n:
        a, b = b, a + b
        if is_prime(b):
            prime_fib.append(b)
    return prime_fib