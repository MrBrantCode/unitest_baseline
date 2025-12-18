"""
QUESTION:
Create a function named `fibonacci(n)` that calculates the Fibonacci sequence iteratively up to the nth element, starting from 0. The function should handle both small and large values of n efficiently. The input is an integer `n` representing the number of elements in the Fibonacci sequence, and the output is a list of integers representing the Fibonacci sequence up to the nth element.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[len(fib_sequence) - 1] + fib_sequence[len(fib_sequence) - 2])
    return fib_sequence