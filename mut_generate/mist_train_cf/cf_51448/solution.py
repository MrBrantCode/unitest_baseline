"""
QUESTION:
Create a recursive function `fibonacci(n)` that calculates the nth Fibonacci number. The function should use recursion and must be used in conjunction with a while loop to print the first five Fibonacci numbers.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)