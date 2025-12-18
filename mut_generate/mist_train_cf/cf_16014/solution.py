"""
QUESTION:
Find the time and space complexity of the `fibonacci` function using Big O notation, given the function is implemented recursively and the input "n" is a positive integer. The function should calculate the nth Fibonacci number.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)