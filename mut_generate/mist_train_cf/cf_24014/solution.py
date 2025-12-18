"""
QUESTION:
Create a recursive function called `fibonacci` that generates the nth Fibonacci number. The function should take an integer `n` as input, where `n` represents the position in the Fibonacci series. The Fibonacci series starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. The function should return the nth Fibonacci number.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)