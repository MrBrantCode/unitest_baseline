"""
QUESTION:
Write a function `fibonacci_sequence(n)` that prints out the Fibonacci sequence up to the nth number, where n is a prime number greater than 100. The function should be able to handle any prime number n.
"""

def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq