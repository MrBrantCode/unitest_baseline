"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number, where the Fibonacci sequence starts at 1. The function should use a recursive approach. The Fibonacci sequence should be printed from 1 up to the number just before 144, with each number on a separate line.
"""

def fibonacci(n): 
    if n <= 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 