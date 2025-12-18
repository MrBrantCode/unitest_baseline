"""
QUESTION:
Write a recursive function `fibonacci(n)` to calculate the nth term of the Fibonacci sequence without using any loops or the 'if' statement. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else n