"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number using recursion. The function should handle potential recursive depth limit errors if `n` is exceedingly large.
"""

def fibonacci(n):
    if n<=0:
        return "Error: The input number must be greater than zero"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)