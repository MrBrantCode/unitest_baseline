"""
QUESTION:
Write a function called `fibonacci(n)` that generates the first `n` numbers in the Fibonacci sequence using recursion only. The input `n` is an integer between 1 and 50 inclusive, and the function should return a list of Fibonacci numbers.
"""

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n-1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq