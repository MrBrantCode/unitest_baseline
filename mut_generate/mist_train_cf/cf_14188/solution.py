"""
QUESTION:
Write a recursive function `fibonacci(n)` to calculate the nth term of the Fibonacci sequence, where n is a positive integer. The function should return the nth term if n is a positive integer, and an error message if n is not a positive integer.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)