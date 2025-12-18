"""
QUESTION:
Create a function named `fibonacci(n)` that calculates the nth Fibonacci number using recursion. The function should handle integers n, where n >= 0, and return the corresponding Fibonacci number. Write the function in a way that it can be called within a loop to print the first 20 Fibonacci numbers.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)