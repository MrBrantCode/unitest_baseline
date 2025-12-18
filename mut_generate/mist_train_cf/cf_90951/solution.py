"""
QUESTION:
Write a function `fibonacci(n)` to find the nth term of the Fibonacci sequence, where `n` is a positive integer. The function should return the nth term if `n` is valid, otherwise return an error message. The Fibonacci sequence starts with 0 as the 1st term and 1 as the 2nd term, and each subsequent term is the sum of the previous two terms.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)