"""
QUESTION:
Write a function named `fibonacci` that uses recursion to calculate the nth number in the Fibonacci sequence. The function should take an integer `n` as input and return the corresponding Fibonacci number. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)