"""
QUESTION:
Write a recursive function `fibonacci_series` that takes a non-negative integer `n` as input, prints the Fibonacci series up to the `n`-th number, and returns the sum of all the Fibonacci numbers in the series. The function should have a time complexity of O(2^n) and should not use any loops or built-in functions like sum() or reduce().
"""

def fibonacci_series(n):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    sum_fib = 0
    for i in range(1, n+1):
        fib = fibonacci(i)
        sum_fib += fib
        print(fib, end=" ")
    return sum_fib