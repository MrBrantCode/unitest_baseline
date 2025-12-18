"""
QUESTION:
Create a function named `fibonacci(n)` that generates a list of Fibonacci sequence up to the nth number. The function should have a time complexity of O(n) and should be efficient in terms of performance. The Fibonacci sequence should start with 0 and 1, and each subsequent number is the sum of the previous two.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        next_val = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_val)
    return fib_sequence