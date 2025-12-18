"""
QUESTION:
Write a function `fibonacci_prime(n)` that takes a positive integer `n` and returns the nth Fibonacci prime number. Use an iterative approach to solve this problem.
"""

def fibonacci_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
    return b