"""
QUESTION:
Write a function named `fibonacci(n)` that generates the Fibonacci sequence up to the nth number using recursion. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence