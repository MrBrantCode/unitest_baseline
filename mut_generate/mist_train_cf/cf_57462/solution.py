"""
QUESTION:
Write a recursive function called `fibonacci` that takes an integer `n` as input and returns a list of the first `n` numbers in the Fibonacci series. The function should use recursion to generate the series.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-2] + fib_list[-1])
        return fib_list