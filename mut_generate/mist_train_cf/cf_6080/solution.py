"""
QUESTION:
Create a function called `fibonacci` that takes a positive integer `n` as input where `1 <= n <= 10^9` and `n` is a prime number. This function should return the Fibonacci sequence up to the nth number. The function should have a time complexity of O(log n) or better.
"""

def fibonacci(n):
    if n <= 0:
        return []
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq