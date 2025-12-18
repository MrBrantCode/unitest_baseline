"""
QUESTION:
Write a function `fibonacci_sequence(N)` that uses recursion to calculate the Fibonacci sequence up to `N`. The function should take an integer `N` as input and return a list of Fibonacci numbers up to `N`. If `N` is less than or equal to 0, the function should return an empty list.
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