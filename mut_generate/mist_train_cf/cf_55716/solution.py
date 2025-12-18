"""
QUESTION:
Write a recursive function called `fibonacci(n)` that calculates the nth value in the Fibonacci sequence, where n is a positive integer. The function should return the calculated value if n is a positive integer, and an error message if n is not a positive integer. The function should use recursion to calculate the nth value by summing the (n-1)th and (n-2)th values in the sequence.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)