"""
QUESTION:
Write a function named `fibonacci(N)` that generates the Fibonacci sequence up to a limit `N`. The function should return a list of Fibonacci numbers where the last number in the list is less than `N`. The limit `N` must be greater than 1.
"""

def fibonacci(N):
    sequence = [0, 1]
    while sequence[-1] < N:
        sequence.append(sequence[-2] + sequence[-1])
    return sequence[:-1]