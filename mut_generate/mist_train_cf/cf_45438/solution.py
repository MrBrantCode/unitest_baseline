"""
QUESTION:
Write a function named `fib` to calculate the 'n'th Fibonacci number, where 'n' is a non-negative integer. The function should handle large inputs (n <= 10^6) efficiently.
"""

def fib(n):
    fib_numbers = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers[n]