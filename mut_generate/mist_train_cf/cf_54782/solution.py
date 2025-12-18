"""
QUESTION:
Write a function called `is_fibonacci` that takes an integer `n` as input and returns "yes" if `n` is a Fibonacci number, "no" if it's not. The function should handle multiple inputs simultaneously and be optimized to work efficiently with larger numbers. If the input is not an integer, the function should return an error message. Implement error handling mechanisms to deal with unexpected inputs.
"""

def is_perfect_square(x):
    if x < 0:
        return False
    sqrt_x = int(x ** 0.5)
    return sqrt_x * sqrt_x == x

def is_fibonacci(n):
    if not isinstance(n, int):
        return "Error: Input is not an integer."
    return "yes" if is_perfect_square(5*n*n+4) or is_perfect_square(5*n*n-4) else "no"