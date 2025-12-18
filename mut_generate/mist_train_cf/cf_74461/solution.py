"""
QUESTION:
Generate a list of Fibonacci numbers within a specified range. Write a function named `fib` that returns the Fibonacci sequence up to a given number `n`. Then, use this function to find all Fibonacci numbers between 100 and 150.
"""

def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while fib_sequence[-1] + fib_sequence[-2] < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence