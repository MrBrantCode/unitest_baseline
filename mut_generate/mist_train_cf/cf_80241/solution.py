"""
QUESTION:
Write a function named `fibonacci` to calculate the nth Fibonacci number. The function should take an integer `n` as input and return the nth Fibonacci number. Analyze the time complexity of the function and explain why it may not be efficient for large values of `n`.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)