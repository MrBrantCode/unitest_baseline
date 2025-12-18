"""
QUESTION:
Write a function `generate_prime_fibonacci(n)` that generates a list of the first `n` prime Fibonacci numbers, where a prime Fibonacci number is a Fibonacci number that is also a prime number. The function should return a list of integers. The input `n` is a positive integer.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_fibonacci(n):
    prime_fibonacci = []
    fib_sequence = [0, 1]
    while len(prime_fibonacci) < n:
        fib_next = fib_sequence[-1] + fib_sequence[-2]
        if is_prime(fib_next):
            prime_fibonacci.append(fib_next)
        fib_sequence.append(fib_next)
    return prime_fibonacci