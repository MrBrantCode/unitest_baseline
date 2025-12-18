"""
QUESTION:
Write a function `fibonacci` that calculates the nth Fibonacci number using recursion with memoization, and a function `reverse_fibonacci` that generates the first n Fibonacci numbers and returns them in reverse order. The `fibonacci` function should not use any loops or built-in functions for calculating the Fibonacci numbers, and should only rely on recursion and memoization.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

def reverse_fibonacci(n):
    fib_list = []
    for i in range(n-1, -1, -1):
        fib_list.append(fibonacci(i))
    return fib_list