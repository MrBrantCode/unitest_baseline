"""
QUESTION:
Create a recursive function named `fibonacci(n)` that calculates the nth Fibonacci number. The function should take one parameter `n`, which represents the position of the Fibonacci number to be calculated. The function should return the nth Fibonacci number if `n` is a positive integer, and return an error message if `n` is not a positive integer. Use this function to calculate the first `max_num` Fibonacci numbers where `max_num` is 5.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)