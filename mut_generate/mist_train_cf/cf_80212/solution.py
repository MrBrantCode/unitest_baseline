"""
QUESTION:
Create a function `fibonacci(n)` that uses recursion to compute the Fibonacci sequence up to the nth number. The function should return a list of the first n numbers in the Fibonacci sequence. If n is 0 or less, the function should return an empty list.
"""

def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fib(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series