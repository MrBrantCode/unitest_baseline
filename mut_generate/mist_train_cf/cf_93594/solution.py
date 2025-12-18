"""
QUESTION:
Implement a function `fibonacci(n)` that generates the nth Fibonacci number using recursion. The function should return the nth Fibonacci number if `n` is a non-negative integer. If `n` is a negative integer, the function should print an error message "Error: Input value cannot be negative." and return without a value.
"""

def fibonacci(n):
    if n < 0:
        print("Error: Input value cannot be negative.")
        return

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)