"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth number in the zero-indexed Fibonacci sequence using recursion. The Fibonacci sequence is defined as a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. The function should return "Input should be a positive integer." if n is less than or equal to 0.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)