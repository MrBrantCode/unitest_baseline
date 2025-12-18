"""
QUESTION:
Create a function named `fib` that takes a positive integer `n` as input and returns the Nth element of the Fibonacci sequence. The function should return an error message if `n` is not a positive integer. The Fibonacci sequence is defined as a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fib(n):
    if n <= 0:
        return "N should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)