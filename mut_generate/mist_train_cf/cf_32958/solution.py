"""
QUESTION:
Create a function `calculate_fibonacci(n)` that calculates the nth Fibonacci number using a recursive approach. The function should return the correct Fibonacci number for a given positive integer `n`. If `n` is less than or equal to 0, the function should return "Invalid input".
"""

def calculate_fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)