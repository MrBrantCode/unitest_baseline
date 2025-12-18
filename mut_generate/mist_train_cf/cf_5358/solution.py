"""
QUESTION:
Write a function called `fibonacci` that returns a list of integers representing the Fibonacci sequence up to the nth number using a recursive algorithm. The function should take an integer `n` as input, where `n` is a positive integer greater than 0. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq