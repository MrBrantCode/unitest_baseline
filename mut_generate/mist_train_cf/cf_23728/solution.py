"""
QUESTION:
Create a function `fibonacci(n)` that generates the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `n` as input and return the corresponding Fibonacci number. Write the function to calculate the first 10 numbers in the Fibonacci series.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)