"""
QUESTION:
Write a recursive function `fibonacci(n)` to calculate the nth term of the Fibonacci sequence where `n` is a positive integer and the sequence starts with 0 and 1. If `n` is not a positive integer, return an error message.
"""

def entance(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return entance(n-1) + entance(n-2)