"""
QUESTION:
Write a function `fibonacci(n)` that generates the first `n` terms of the Fibonacci sequence. The input `n` is guaranteed to be a prime number. The Fibonacci sequence should start with the initial terms `[0, 1]` and each subsequent term should be the sum of the two preceding ones.
"""

def fibonacci(n):
    fib_seq = [0, 1]  # Initial terms of the Fibonacci sequence

    # Generate Fibonacci sequence until it reaches the desired length
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq