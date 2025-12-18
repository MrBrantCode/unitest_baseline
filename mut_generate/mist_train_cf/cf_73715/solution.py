"""
QUESTION:
Design a function named `fibonacci` that takes a positive integer `n` as input and returns the first `n` terms of the Fibonacci sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq