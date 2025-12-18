"""
QUESTION:
Write a function named `fibonacci` that calculates the nth Fibonacci number using recursion. The function should take an integer `n` as input and return the nth Fibonacci number. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case: calculate the Fibonacci number by adding the previous two numbers in the sequence
    else:
        return fibonacci(n-1) + fibonacci(n-2)