"""
QUESTION:
Write a function `factorial_fibonacci(n)` that generates the Fibonacci series up to the given number `n` (excluding `n` if it's not a part of the series) and returns a list of the factorials of each number in the series. Use the `math.factorial()` function from the `math` module to calculate the factorials. The function should be able to handle any positive integer `n`.
"""

import math

def factorial_fibonacci(n):
    fib_series = [0, 1]
    while fib_series[-1] < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    fib_series = fib_series[:-1]  # excluding 'n' from the series if 'n' is not a part of the series
    return [math.factorial(i) for i in fib_series]