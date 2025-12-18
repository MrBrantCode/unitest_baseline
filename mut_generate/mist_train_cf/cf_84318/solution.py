"""
QUESTION:
Write a function named `fibo_series` that generates the Fibonacci series up to the nth number. The function should take an integer `n` as input and return a list of integers representing the first `n` numbers in the Fibonacci series. The function should handle inputs less than or equal to zero by returning the string "Input should be positive int."
"""

def fibo_series(n):
    if n <= 0:
        return "Input should be positive int."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series