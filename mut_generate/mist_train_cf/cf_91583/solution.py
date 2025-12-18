"""
QUESTION:
Create a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth number. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence.
"""

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq