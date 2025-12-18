"""
QUESTION:
Write a function `prime_fibonacci_squares(n)` that takes a positive integer `n` as input and returns a tuple containing a list of the squares of the first `n` prime numbers that are also Fibonacci numbers, and the product of these squares.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fibonacci_squares(n):
    prime_fib_squares = []
    a, b = 0, 1
    while len(prime_fib_squares) < n:
        a, b = b, a + b
        if is_prime(a) and a != 0 and a != 1:
            prime_fib_squares.append(a ** 2)
    product = 1
    for square in prime_fib_squares:
        product *= square
    return prime_fib_squares, product