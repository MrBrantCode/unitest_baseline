"""
QUESTION:
Write a function named `fibonacci_prime` that takes a positive integer `n` as input and returns the nth Fibonacci prime number. The function should use an iterative approach and assume that `n` will always be a positive integer.
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
    while True:
        a, b = b, a + b
        if is_prime(b) and b > 1:
            count += 1
            if count == n:
                return b