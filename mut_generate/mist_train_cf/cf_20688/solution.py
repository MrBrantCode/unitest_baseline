"""
QUESTION:
Write a function named `fibonacci(n)` that calculates the Fibonacci number at a given position `n`. The function should take an integer `n` as input, where `n` is a positive integer between 1 and 10^6 (inclusive). The function should return the Fibonacci number at position `n`. The time complexity of the function should be O(n) or better.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq[-1]