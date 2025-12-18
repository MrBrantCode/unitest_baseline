"""
QUESTION:
Design a function called `fibonacci_sequence` that takes an integer `n` as input and returns a list of Fibonacci sequence numbers up to the `n`th number. If `n` is negative or zero, return an empty list. Implement the function using a single loop and achieve a time complexity of O(n), not O(log(n)).
"""

def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_seq = [0, 1]

    if n <= 1:
        return fib_seq[:n+1]

    while len(fib_seq) <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq