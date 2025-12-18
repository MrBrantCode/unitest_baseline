"""
QUESTION:
Create a function named `fibonacci` that generates a Fibonacci sequence of 'n' numbers. The function should take an integer 'n' as input and return a list of the first 'n' Fibonacci numbers. If 'n' is 0 or negative, the function should return an empty list.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence