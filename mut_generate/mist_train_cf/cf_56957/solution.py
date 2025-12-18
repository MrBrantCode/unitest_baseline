"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given number. The function should take one argument `n`. If `n` is not an integer, the function should return the error message "Error: Input must be an integer." If `n` is a negative integer, the function should return the error message "Error: Factorial of negative numbers is undefined." Otherwise, the function should calculate and return the factorial of `n`.
"""

def factorial(n):
    # Check if n is an integer
    if not isinstance(n, int):
        return "Error: Input must be an integer"
    # Factorial of negative numbers is undefined
    elif n < 0:
        return "Error: Factorial of negative numbers is undefined."
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact