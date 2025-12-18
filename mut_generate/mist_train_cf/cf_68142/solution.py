"""
QUESTION:
Write a function named `fibonacci(n)` that generates the Fibonacci sequence up to 'n' iterations, where each number in the sequence is the sum of the two preceding ones, starting with 0 and 1. The function should return the Fibonacci sequence as a list.
"""

def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq