"""
QUESTION:
Write a function `fib(n)` that calculates the Fibonacci sequence up to the n-th term. The function should be efficient for larger values of 'n', handle negative input values by returning an error message, and handle floating-point input values by rounding down to the nearest integer. The function should return a list of integers representing the Fibonacci sequence.
"""

def fib(n):
    if n < 0:
        return "Invalid input"
    elif type(n) == float:
        n = int(n)
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq