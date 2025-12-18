"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given number without using recursion, in-built functions, or external libraries. The function should take one argument `n` and return the factorial of `n` if `n` is a non-negative integer. If `n` is not an integer or is a negative integer, the function should return an error message.
"""

def factorial(n):
    # Check if n is a non-integer
    if not isinstance(n, int):
        return "Error: Input is not an integer."
    # Check if n is a negative integer
    elif n < 0:
        return "Error: Input is a negative integer."
    else:
        fact = 1
        # calculate factorial
        for i in range(1, n + 1):
            fact = fact * i
        return fact