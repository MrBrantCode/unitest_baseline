"""
QUESTION:
Write a function `fibonacci(n)` that takes an integer `n` as input and returns a list of Fibonacci numbers up to the `n`th number, and a function `factorial(n)` that takes an integer `n` as input and returns the factorial of `n`. The Fibonacci sequence is defined such that each subsequent number is the sum of the two preceding numbers, and the factorial of a number `n` is the product of all positive integers less than or equal to `n`. Implement these functions using recursion. Ensure that `n` is a positive integer.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n-1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)