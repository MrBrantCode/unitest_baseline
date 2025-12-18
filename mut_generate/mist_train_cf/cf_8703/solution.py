"""
QUESTION:
Write a function `fibonacci_sum(n)` that calculates the sum of Fibonacci numbers less than or equal to `n` that are multiples of 3, given that `n` is a prime number and a multiple of 3.
"""

def fibonacci_sum(n):
    fib_numbers = [0, 1]
    fib_sum = 1
    while fib_numbers[-1] < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        if fib_numbers[-1] % 3 == 0:
            fib_sum += fib_numbers[-1]
    return fib_sum