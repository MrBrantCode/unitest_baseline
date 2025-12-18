"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns a list of Fibonacci numbers up to the nth number, with a time complexity of O(n).
"""

def fibonacci(n):
    if n <= 0:
        return []

    fib_sequence = [0, 1]  

    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence