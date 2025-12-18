"""
QUESTION:
Create a function called `fibonacci(n)` that generates the Fibonacci sequence up to the nth position. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence. The Fibonacci sequence should start with 0 and 1, and each subsequent number should be the sum of the previous two numbers. The sequence should have a length of `n`. The position is zero-indexed, meaning the first position is 0.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence