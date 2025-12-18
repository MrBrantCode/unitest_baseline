"""
QUESTION:
Write a function `fibonacci(n)` that takes a positive integer `n` as input and returns the nth element of the Fibonacci sequence. The input `n` should be less than or equal to 100.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input. n should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq[-1]