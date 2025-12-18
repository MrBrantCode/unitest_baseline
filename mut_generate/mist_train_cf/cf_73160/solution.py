"""
QUESTION:
Create a function `factorial_recursive(n)` that calculates the factorial of a non-negative integer `n` using recursion. 

Create another function `factorial_error_handler(n)` that calls `factorial_recursive(n)` if the input `n` is a non-negative integer, and returns an informative error message if `n` is not an integer or is negative.
"""

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorial_error_handler(n):
    if type(n) is not int:
        return "Error: Input is not an integer."
    elif n < 0:
        return "Error: Input is a negative number."
    else:
        return factorial_recursive(n)