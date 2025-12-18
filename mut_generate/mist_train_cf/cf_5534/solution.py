"""
QUESTION:
Write a function named `calculate_factorial` that takes an integer `n` as input and returns its factorial. You are not allowed to use the built-in factorial function or any external libraries. The function should be able to handle large numbers efficiently.
"""

def calculate_factorial(n):
    # Initialize the result as 1
    result = 1

    # Multiply the result with numbers from 1 to n
    for i in range(1, n + 1):
        result *= i

    return result