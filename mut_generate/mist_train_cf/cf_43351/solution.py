"""
QUESTION:
Develop a function `fibonacci(n)` that generates the nth term of the Fibonacci sequence using recursion. The function should take an integer `n` as input and return the nth term of the Fibonacci sequence. The function should include error handling to ensure that `n` is a positive integer.
"""

def fibonacci(n):
    if n <= 0:
        return "Error: Input should be a positive integer."
    elif n == 1: 
        return 0
    elif n == 2: 
        return 1  
    else:
        return fibonacci(n-1) + fibonacci(n-2)