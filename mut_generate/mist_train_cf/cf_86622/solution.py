"""
QUESTION:
Write a Python function `fibonacci_sequence` that calculates the Fibonacci sequence up to a given limit, N. The function should take an integer N as input and return a list of Fibonacci numbers up to N. The function should handle N being less than or equal to 0 by returning an empty list. The Fibonacci sequence should be calculated using recursion only, without any loops or iterative methods.
"""

def fibonacci_sequence(N):
    if N <= 0:
        return []
    elif N == 1:
        return [0]
    elif N == 2:
        return [0, 1]
    else:
        sequence = fibonacci_sequence(N-1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence[:N]