"""
QUESTION:
Create a function named `fibonacci` that takes a positive integer `n` as input and returns a list of the first `n` numbers in the Fibonacci sequence using only recursion, without any loops. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n-1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq