"""
QUESTION:
Write a function `fibonacci_mod` that takes two integers `n` and `m` as input and returns the `n`-th Fibonacci number modulo `m`. The Fibonacci sequence starts with 1, 1, and each subsequent term is the sum of the two preceding ones. The function should use a space-efficient approach to calculate the result for large values of `n`.
"""

def fibonacci_mod(n, m):
    fib_sequence = [0, 1]
    
    for _ in range(2, n+1):
        fib_sequence.append((fib_sequence[-1] + fib_sequence[-2]) % m)

    return fib_sequence[n]