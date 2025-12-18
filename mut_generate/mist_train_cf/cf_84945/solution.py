"""
QUESTION:
Create a function named `generate_fibonacci` that generates a Fibonacci series up to a given number `n`. The function should return a list of Fibonacci numbers where the last number is less than `n`.
"""

def generate_fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:-1]